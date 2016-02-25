#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
from moveit_commander import MoveGroupCommander
from geometry_msgs.msg import PoseStamped, Quaternion
from tf.transformations import quaternion_from_euler

ARM_GROUP = "arm"
START_POSITION = "start_position"


class CobraMove:
    def __init__(self):

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('cobra_move_cartesian', anonymous=True)

        arm = MoveGroupCommander(ARM_GROUP)

        arm.allow_replanning(True)
        # arm.set_goal_position_tolerance(0.01)

        arm.set_named_target(START_POSITION)
        arm.go()
        rospy.sleep(2)

        waypoints = list()

        pose = PoseStamped().pose

        # start with the current pose
        waypoints.append(copy.deepcopy(arm.get_current_pose(arm.get_end_effector_link()).pose))

        # same orientation for all
        q = quaternion_from_euler(0.0, 0.0, 0.0)  # roll, pitch, yaw
        pose.orientation = Quaternion(*q)

        # first pose
        pose.position.x = 0.35
        pose.position.y = 0.25
        pose.position.z = 0.3
        waypoints.append(copy.deepcopy(pose))

        # second pose
        pose.position.x = 0.25
        pose.position.y = -0.3
        pose.position.z = 0.3
        waypoints.append(copy.deepcopy(pose))

        # third pose
        pose.position.x += 0.15
        waypoints.append(copy.deepcopy(pose))

        # fourth pose
        pose.position.y += 0.15
        waypoints.append(copy.deepcopy(pose))

        (plan, fraction) = arm.compute_cartesian_path(
                                  waypoints,   # waypoints to follow
                                  0.01,        # eef_step
                                  0.0)         # jump_threshold

        print "====== waypoints created ======="
        # print waypoints

        # ======= show cartesian path ====== #
        arm.go()
        rospy.sleep(10)

        print "========= end ========="

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__=='__main__':
    CobraMove()
