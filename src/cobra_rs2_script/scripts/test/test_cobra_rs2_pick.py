#! /usr/bin/env python
#
#######
# Basis:
# https://github.com/awesomebytes/moveit_grasping_testing/blob/master/src/moveit_grasping_testing/pick_as_moveit.py
#
#
#
#######
import rospy
import sys
import copy
import moveit_commander
from moveit_commander import PlanningSceneInterface, MoveGroupCommander
import actionlib
from geometry_msgs.msg import PoseStamped, Vector3, Quaternion
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory
from moveit_msgs.msg import Grasp, PickupAction, PickupGoal, GripperTranslation, MoveItErrorCodes
from tf.transformations import quaternion_from_euler

REFERENCE_LINK = "base_link"
START_POSITION = "start_position"
PLANNING_GROUP = "arm"
PICK_OBJECT = "part"
TABLE_OBJECT = "table"
END_EFFECTOR = "hand_tool"
GRIPPER_JOINTS = "gripper_finger_one"

moveit_error_dict = {}

for name in MoveItErrorCodes.__dict__.keys():
    if not name[:1] == '_':
        code = MoveItErrorCodes.__dict__[name]
        moveit_error_dict[code] = name


def get_grasp_posture(pre):
    pre_grasp_posture = JointTrajectory()
    pre_grasp_posture.header.frame_id = END_EFFECTOR
    pre_grasp_posture.header.stamp = rospy.Time.now()
    pre_grasp_posture.joint_names = [GRIPPER_JOINTS]
    pos = JointTrajectoryPoint()
    if pre:  # gripper open
        pos.positions = [0.0]
    else:  # gripper closed
        pos.positions = [0.04]
    pre_grasp_posture.points.append(pos)
    return pre_grasp_posture


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


def create_grasp(grasp_pose, allowed_touch_objects=[], pre_grasp_posture=None, grasp_posture=None,
                 pre_grasp_approach=None, post_grasp_retreat=None, id_grasp="grasp_"):
    grasp = Grasp()
    grasp.id = id_grasp
    grasp.grasp_pose = grasp_pose
    if pre_grasp_posture is None:
        grasp.pre_grasp_posture = get_grasp_posture(True)
    else:
        grasp.pre_grasp_posture = pre_grasp_posture

    if grasp_posture is None:
        grasp.grasp_posture = get_grasp_posture(False)
    else:
        grasp.grasp_posture = grasp_posture

    grasp.allowed_touch_objects = allowed_touch_objects

    if pre_grasp_approach is not None:
        grasp.pre_grasp_approach = pre_grasp_approach

    if post_grasp_retreat is not None:
        grasp.post_grasp_retreat = post_grasp_retreat

    grasp.max_contact_force = 0

    return grasp


def create_random_grasps(grasp_pose, num_grasps=1):
    list_grasps = []
    for grasp_num in range(num_grasps):
        my_pre_grasp_approach = create_gripper_translation(Vector3(0.0, 0.0, -1.0))  # take object along neg z-axis
        my_post_grasp_retreat = create_gripper_translation(Vector3(0.0, 0.0, 1.0))  # go with object along pos z-axis
        header = Header()
        header.frame_id = REFERENCE_LINK
        header.stamp = rospy.Time.now()
        grasp_pose_copy = copy.deepcopy(grasp_pose)
        modified_grasp_pose = PoseStamped(header, grasp_pose_copy)
        grasp = create_grasp(modified_grasp_pose,
                             allowed_touch_objects=[PICK_OBJECT],
                             pre_grasp_posture=get_grasp_posture(True),
                             grasp_posture=get_grasp_posture(True),
                             pre_grasp_approach=my_pre_grasp_approach,
                             post_grasp_retreat=my_post_grasp_retreat,
                             id_grasp="random_grasp_" + str(grasp_num)
                             )
        list_grasps.append(grasp)
    return list_grasps


def create_pickup_goal(group=PLANNING_GROUP, target=PICK_OBJECT, grasp_pose=PoseStamped(), possible_grasps=[]):
    pug = PickupGoal()
    pug.target_name = target
    pug.group_name = group
    pug.possible_grasps.extend(possible_grasps)

    # configure
    pug.allowed_planning_time = 5.0
    pug.planning_options.planning_scene_diff.is_diff = True
    pug.planning_options.planning_scene_diff.robot_state.is_diff = True
    pug.planning_options.plan_only = False
    pug.planning_options.replan = True
    pug.planning_options.replan_attempts = 10
    return pug


if __name__ == '__main__':

    # Initialize the move_group API
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("cobra_test_pick")

    arm = MoveGroupCommander(PLANNING_GROUP)

    # Action Clients for Pick
    rospy.loginfo("Connecting to pickup AS")
    pickup_ac = actionlib.SimpleActionClient('/pickup', PickupAction)
    pickup_ac.wait_for_server()
    rospy.loginfo("Successfully connected")

    # create Planning Scene
    scene = PlanningSceneInterface()
    rospy.sleep(1)
    i = 1
    while i <= 10:

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
        p.pose.position.x = 0.4
        p.pose.position.y = 0.0
        p.pose.position.z = 0.15
        # add part
        scene.add_box(PICK_OBJECT, p, (0.07, 0.07, 0.1))
        rospy.loginfo("Added objects to world")

        rospy.sleep(1)

        pose_grasp = copy.deepcopy(p)

        # create list of grasps
        possible_grasps = create_random_grasps(pose_grasp.pose, 100)

        # create goal for pick
        goal = create_pickup_goal(PLANNING_GROUP, PICK_OBJECT, pose_grasp, possible_grasps)
        rospy.loginfo("Sending goal")
        pickup_ac.send_goal(goal)

        rospy.loginfo("Waiting for result")
        pickup_ac.wait_for_result()
        result = pickup_ac.get_result()

        rospy.loginfo("Pick Result is:")
        rospy.loginfo("Human readable error: " + str(moveit_error_dict[result.error_code.val]))
        rospy.sleep(5)

         # clean world
        rospy.loginfo("Cleaning world objects")
        scene.remove_world_object(TABLE_OBJECT)
        scene.remove_world_object(PICK_OBJECT)
        scene.remove_attached_object(arm.get_end_effector_link(), PICK_OBJECT)
        rospy.sleep(2)
        i += 1

    # end
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
