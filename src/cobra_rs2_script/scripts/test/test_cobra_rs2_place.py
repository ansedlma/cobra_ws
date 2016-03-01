#! /usr/bin/env python
#
#######
# Basis:
# https://github.com/awesomebytes/moveit_grasping_testing/blob/master/src/moveit_grasping_testing/place_object.py
#
#
#
#######
import copy
import math
import rospy
import sys
import moveit_commander
from moveit_commander import MoveGroupCommander, PlanningSceneInterface
import actionlib
from geometry_msgs.msg import PoseStamped, Vector3, Quaternion
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory
from moveit_msgs.msg import GripperTranslation, MoveItErrorCodes, PlaceAction, PlaceGoal, PlaceLocation
from tf.transformations import quaternion_from_euler

REFERENCE_LINK = "base_link"
PLANNING_GROUP = "arm"
PICK_OBJECT = "part"
TABLE_OBJECT = "table"
END_EFFECTOR = "hand_tool"
GRIPPER_JOINTS = ["gripper_finger_one"]

moveit_error_dict = {}

for name in MoveItErrorCodes.__dict__.keys():
    if not name[:1] == '_':
        code = MoveItErrorCodes.__dict__[name]
        moveit_error_dict[code] = name


def create_gripper_translation(direction_vector, desired_distance=0.15, min_distance=0.01):
    g_trans = GripperTranslation()
    g_trans.direction.header.frame_id = REFERENCE_LINK
    g_trans.direction.header.stamp = rospy.Time.now()
    g_trans.direction.vector.x = direction_vector.x
    g_trans.direction.vector.y = direction_vector.y
    g_trans.direction.vector.z = direction_vector.z
    g_trans.desired_distance = desired_distance
    g_trans.min_distance = min_distance
    return g_trans


# Generate a place locations
def generate_place_locations( position):
    pls = []
    pl = PlaceLocation()
    pl.place_pose = position
    for x in range(0, 360, 2):
        quat = quaternion_from_euler(0.0, 0.0, round(math.radians(x), 4))
        pl.place_pose.pose.orientation = Quaternion(*quat)
        # take object along negative z-axis
        pl.pre_place_approach = create_gripper_translation(Vector3(0.0, 0.0, -1.0))
        # go with object along positive z-axis
        pl.post_place_retreat = create_gripper_translation(Vector3(0.0, 0.0, 1.0))

        pl.post_place_posture = get_post_place_posture()
        pls.append(copy.deepcopy(pl))
        return pls


def get_post_place_posture():
    pre_grasp_posture = JointTrajectory()
    pre_grasp_posture.header.frame_id = END_EFFECTOR
    pre_grasp_posture.header.stamp = rospy.Time.now()
    pre_grasp_posture.joint_names = GRIPPER_JOINTS
    pos = JointTrajectoryPoint()  # open gripper
    pos.positions = [0.0]
    pre_grasp_posture.points.append(pos)
    return pre_grasp_posture


def place(group, target, place_position):
    # Obtain possible places
    place_locs = generate_place_locations(place_position)

    # create and send place goal
    goal_place = create_place_goal(group, target, place_locs)

    place_ac.send_goal(goal_place)
    place_ac.wait_for_result()
    result_goal = place_ac.get_result()
    return result_goal


def create_place_goal(group, target, places):
    # create goal
    goal = PlaceGoal()
    goal.group_name = group
    goal.attached_object_name = target
    goal.place_locations.extend(places)

    # configure
    goal.allowed_planning_time = 5.0
    goal.planning_options.planning_scene_diff.is_diff = True
    goal.planning_options.planning_scene_diff.robot_state.is_diff = True
    goal.planning_options.plan_only = False
    goal.planning_options.replan = True
    goal.planning_options.replan_attempts = 10
    goal.allow_gripper_support_collision = False
    return goal


def generate_place_pose():
    pp = PoseStamped()
    pp.header.frame_id = REFERENCE_LINK
    pp.header.stamp = rospy.Time.now()
    pp.pose.position.x = 0.45
    pp.pose.position.y = 0.0
    pp.pose.position.z = 0.15
    pq = quaternion_from_euler(0.0, 0.0, 0.0)
    pp.pose.orientation = Quaternion(*pq)
    return pp


def generate_rand_position():
    rand_pos = arm.get_random_pose(arm.get_end_effector_link())
    rp = PoseStamped()
    rp.header.frame_id = REFERENCE_LINK
    rp.header.stamp = rospy.Time.now()
    rp.pose.position.x = rand_pos.pose.position.x
    rp.pose.position.y = rand_pos.pose.position.y
    rp.pose.position.z = rand_pos.pose.position.z
    rq = quaternion_from_euler(0.0, 0.0, 0.0)
    rp.pose.orientation = Quaternion(*rq)
    return rp


if __name__=='__main__':

    # Initialize the move_group API
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("cobra_test_place")

    arm = MoveGroupCommander(PLANNING_GROUP)

    # # tolerance
    # arm.set_goal_position_tolerance(0.01)
    # arm.set_goal_orientation_tolerance(0.01)
    # arm.set_goal_joint_tolerance(0.01)
    # arm.set_goal_tolerance(0.01)

    # Action Clients for Place
    rospy.loginfo("Connecting to place AS")
    place_ac = actionlib.SimpleActionClient('/place', PlaceAction)
    place_ac.wait_for_server()
    rospy.loginfo("Successfully connected")

    # create Planning Scene
    scene = PlanningSceneInterface()
    rospy.sleep(1)

    # publish a demo scene
    p = PoseStamped()
    p.header.frame_id = REFERENCE_LINK
    p.header.stamp = rospy.Time.now()

    quat = quaternion_from_euler(0.0, 0.0, 0.0)  # roll, pitch, yaw
    p.pose.orientation = Quaternion(*quat)

    p.pose.position.x = 0.6
    p.pose.position.y = 0.0
    p.pose.position.z = 0.0
    # add table
    scene.add_box(TABLE_OBJECT, p, (0.5, 0.5, 0.2))

    i = 1
    while i <= 10:

        gripper_pose = arm.get_current_pose(arm.get_end_effector_link())
        # part
        p.pose.position.x = gripper_pose.pose.position.x
        p.pose.position.y = gripper_pose.pose.position.y
        p.pose.position.z = gripper_pose.pose.position.z
        # add part
        scene.add_box(PICK_OBJECT, p, (0.07, 0.07, 0.1))
        rospy.loginfo("Added object to world")

        # attach object manually
        arm.attach_object(PICK_OBJECT, arm.get_end_effector_link(), GRIPPER_JOINTS)
        rospy.sleep(1)

        #  ===== place start ==== #
        place_result = place(PLANNING_GROUP, PICK_OBJECT, generate_place_pose())

        rospy.loginfo("Place Result is:")
        rospy.loginfo("Human readable error: " + str(moveit_error_dict[place_result.error_code.val]))
        rospy.sleep(5)

        # remove part
        scene.remove_world_object(PICK_OBJECT)
        scene.remove_attached_object(arm.get_end_effector_link(), PICK_OBJECT)
        rospy.sleep(2)
        i += 1

    # end
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
