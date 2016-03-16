#! /usr/bin/env python

import copy

import math
import rospy
from geometry_msgs.msg import Vector3
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory
from moveit_msgs.msg import PlaceLocation, GripperTranslation
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Quaternion
from std_msgs.msg import Header
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from numpy import arange

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

REFERENCE_FRAME = "base_link"
EEF_LINK = "hand_pipe"
GRIPPER_JOINTS = ["gripper_finger_one"]


class PlaceManager:
    def __init__(self, planning_group, pick_and_place_interface, config, debug=0):
        print "[INFO] Initialise Place Move"
        self.DEBUG = debug
        self.pick_and_place_interface = pick_and_place_interface
        self.arm = planning_group

        # initialise place publisher
        self.place_publisher = rospy.Publisher("generated_places", PoseArray)

        # config
        self.disk_height = config.disk_height
        self.tower_positions = config.tower_positions

    """This method publishes the place poses as a PoseArray.
    :param places: PoseStamped of place poses
    """
    def publish_place_as_pose(self, places):
        if self.DEBUG is 1:
            print "[DEBUG] Publishing PoseArray on /place_pose"
        place_pose = PoseArray()
        # header
        header = Header()
        header.frame_id = REFERENCE_FRAME
        header.stamp = rospy.Time.now()
        place_pose.header = header
        for place_location in places:
            # append position
            p = Pose(place_location.place_pose.pose.position, place_location.place_pose.pose.orientation)
            place_pose.poses.append(copy.deepcopy(p))
        # publish
        self.place_publisher.publish(place_pose)
        if self.DEBUG is 1:
            print '[DEBUG] Published ' + str(len(place_pose.poses)) + ' poses'

    """This method generates the gripper translation message (pre_place_approach and post_place_retreat)
    with a direction vector, the desired distance and the min distance. This is needed to generate a
    PlaceLocation message.
    :param direction_vector: the direction vector
    :param desired_distance: the desired distance
    :param min_distance: the min distance
    :returns: the gripper translation message
    """
    @staticmethod
    def create_gripper_translation(direction_vector, desired_distance=0.10, min_distance=0.05):
        gt = GripperTranslation()
        gt.direction.header.frame_id = REFERENCE_FRAME
        gt.direction.header.stamp = rospy.Time.now()
        gt.direction.vector.x = direction_vector.x
        gt.direction.vector.y = direction_vector.y
        gt.direction.vector.z = direction_vector.z
        gt.desired_distance = desired_distance
        gt.min_distance = min_distance
        return gt

    """This method generates place locations.
    :param init_pose: the desired pose
    :returns: the PlaceLocation message
    """
    def generate_place_locations(self, goal_pose):
        pls = []
        # get euler axis values
        axis = euler_from_quaternion([goal_pose.pose.orientation.x, goal_pose.pose.orientation.y,
                                      goal_pose.pose.orientation.z, goal_pose.pose.orientation.w])

        tolerance = round(math.pi/3, 4)
        step = 0.01
        z_axis_angle = round(axis[2], 4)
        # create a range of possible place locations
        for x in arange(round((z_axis_angle - tolerance), 0), round((z_axis_angle + tolerance), 0), step, dtype=float):
        # for x in arange(0, 360, step, dtype=float):
            pl = PlaceLocation()
            pl.place_pose = goal_pose
            quat = quaternion_from_euler(0.0, 0.0, round(x, 4))
            pl.place_pose.pose.orientation = Quaternion(*quat)
            # gripper comes from negative z axis
            pl.pre_place_approach = self.create_gripper_translation(Vector3(0.0, 0.0, -1.0))
            # gripper leaves place position on positive z axis
            pl.post_place_retreat = self.create_gripper_translation(Vector3(0.0, 0.0, 1.0))
            # gripper joint values
            pl.post_place_posture = self.get_post_place_posture()
            pls.append(copy.deepcopy(pl))
        return pls

    """This method generates a JointTrajectory message with the information
    about the links and joints of the gripper. This is needed to complete the
    PlaceLocation message.
    :returns: the JointTrajectory message (post_place_posture)
    """
    @staticmethod
    def get_post_place_posture():
        post_place_posture = JointTrajectory()
        post_place_posture.header.frame_id = EEF_LINK
        post_place_posture.header.stamp = rospy.Time.now()
        post_place_posture.joint_names = GRIPPER_JOINTS
        pos = JointTrajectoryPoint()  # gripper open after place
        pos.positions = [0.0]
        post_place_posture.points.append(pos)
        return post_place_posture

    """This method generates a PoseStamped for the given position and orientation.
    :param position: the desired position of the disk
    :param rad: the orientation of the disk
    :returns: the desired pose
    """
    @staticmethod
    def generate_pose(position, rad=0.0):
        p = PoseStamped()
        p.header.frame_id = REFERENCE_FRAME
        p.header.stamp = rospy.Time.now()

        p.pose.position.x = position[0]
        p.pose.position.y = position[1]
        # to avoid a crash: 2mm distance
        p.pose.position.z = position[2] + 0.002
        q = quaternion_from_euler(0.0, 0.0, rad)
        p.pose.orientation = Quaternion(*q)
        return p

    """This method puts all the information together and starts
    the place action via the pick and place interface.
    :param tower: the destination tower
    :param disk: the attached disk
    """
    def place(self, tower, disk):
        # set start state before move action
        self.arm.set_start_state_to_current_state()
        # calculate new position of disk
        position = self.generate_next_position(tower)
        if self.DEBUG is 1:
            print "[DEBUG] Place disk position: ", position
        # generate place pose
        place_pose = self.generate_pose(position, tower.get_rad())
        # generate place location
        place_locations = self.generate_place_locations(place_pose)
        # publish for RViz
        self.publish_place_as_pose(place_locations)
        # execute place action with pick and place interface
        self.pick_and_place_interface.place_with_retry(disk.get_id(), place_locations)
        # put disk on destination tower
        tower.put(disk)

    """The method calculates the next position of the attached disk.
    :param tower: the new parent tower of the attached disk
    """
    def generate_next_position(self, tower):
        # how many disk on tower
        disk_number_offset_mul = tower.get_size()
        position = copy.deepcopy(tower.get_position())
        # tower height + (number of disks * disk height) + disk height / 2
        position[2] = round(((self.tower_positions[tower.get_id() - 1][2] * 2) +
                             (self.disk_height * disk_number_offset_mul) + (self.disk_height / 2)), 4)
        return position
