#! /usr/bin/env python

from moveit_msgs.msg import PickupAction
import rospy
from actionlib import SimpleActionClient
import actionlib
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Quaternion
from std_msgs.msg import Header
from moveit_simple_grasps.msg import GenerateGraspsAction, GenerateGraspsGoal
from tf.transformations import quaternion_from_euler

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

REFERENCE_FRAME = "base_link"


class PickManager:
    def __init__(self, planning_group, pick_and_place_interface, debug=0):
        print "[INFO] Initialise Pick Move"
        self.DEBUG = debug
        self.pick_and_place_interface = pick_and_place_interface
        self.arm = planning_group
        # simple action server
        self.pickup_ac = actionlib.SimpleActionClient('/pickup', PickupAction)
        self.grasps_ac = SimpleActionClient('/moveit_simple_grasps_server/generate', GenerateGraspsAction)
        # grasps publisher
        self.grasp_publisher = rospy.Publisher("generated_grasps", PoseArray)

    """This method communicates with the simple grasps server and
    receives some calculated grasps.
    :param pose: the position and orientation of the disk
    :param width: the diameter of the disk
    :returns: a list of grasps
    """
    def generate_grasps(self, pose, width):
        self.grasps_ac.wait_for_server()
        if self.DEBUG is 1:
            print "[DEBUG] Successfully connected."
        goal = GenerateGraspsGoal()
        goal.pose = pose.pose
        goal.width = width
        self.grasps_ac.send_goal(goal)
        if self.DEBUG is 1:
            print "[DEBUG] Sent goal, waiting:\n" + str(goal)
        t_start = rospy.Time.now()
        self.grasps_ac.wait_for_result()
        t_end = rospy.Time.now()
        t_total = t_end - t_start
        if self.DEBUG is 1:
            print "[DEBUG] Result received in " + str(t_total.to_sec())
        grasps = self.grasps_ac.get_result().grasps
        return grasps

    """This method publishes the generated grasps as a PoseArray to the ROS System.
    :param grasps: the generated grasps
    """
    def publish_grasps_as_poses(self, grasps):
        if self.DEBUG is 1:
            print "[DEBUG] Publishing PoseArray on /grasp_pose for grasp_pose"
        pa = PoseArray()
        # header
        header = Header()
        header.frame_id = REFERENCE_FRAME
        header.stamp = rospy.Time.now()
        pa.header = header
        # append all poses to pose array
        for msg in grasps:
            p = Pose(msg.grasp_pose.pose.position, msg.grasp_pose.pose.orientation)
            pa.poses.append(p)

        # publish
        self.grasp_publisher.publish(pa)
        if self.DEBUG is 1:
            print '[DEBUG] Published ' + str(len(pa.poses)) + ' poses'
        rospy.sleep(2)

    """This method generated a pose for the pick action.
    :param position: the position of the disk
    :param rad: the orientation of the parent tower
    :returns: the pick pose
    """
    @staticmethod
    def generate_pose(position, rad=0.0):
        p = PoseStamped()
        p.header.frame_id = REFERENCE_FRAME
        p.header.stamp = rospy.Time.now()

        p.pose.position.x = position[0]
        p.pose.position.y = position[1]
        p.pose.position.z = position[2]
        q = quaternion_from_euler(0.0, 0.0, rad)
        p.pose.orientation = Quaternion(*q)
        return p

    """This method calls the needed functions to generate grasps for picking
    the disk from the tower.
    :param tower: the parent tower of the disk
    :returns: the attached disk
    """
    def pick(self, tower):
        # set start state before move action
        self.arm.set_start_state_to_current_state()
        # get disk on top
        disk = tower.pop()
        # generate pick pose
        pick_pose = self.generate_pose(disk.get_position(), tower.get_rad())
        # call simple grasps server for some grasps
        grasp_list = self.generate_grasps(pick_pose, disk.get_diameter())
        if self.DEBUG is 1:
            print '[DEBUG] Generated ' + str(len(grasp_list)) + ' grasps.'
        # publish generated grasps
        self.publish_grasps_as_poses(grasp_list)
        # start the action
        self.pick_and_place_interface.pick_with_retry(disk.get_id(), grasp_list)
        return disk
