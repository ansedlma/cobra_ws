#!/usr/bin/env python

import sys
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
        rospy.init_node('cobra_move_position', anonymous=True)

        arm = MoveGroupCommander(ARM_GROUP)

        arm.allow_replanning(True)
        arm.set_planning_time(10)

        arm.set_named_target(START_POSITION)
        arm.go()
        rospy.sleep(2)

        print "======== create new goal position ========"

        start_pose = PoseStamped()
        start_pose.header.frame_id = arm.get_planning_frame()

        # Test Position
        start_pose.pose.position.x = 0.2  # 20 cm
        start_pose.pose.position.y = -0.11  # -11 cm
        start_pose.pose.position.z = 0.6  # 60 cm
        q = quaternion_from_euler(0.0, 0.0, 0.0)
        start_pose.pose.orientation = Quaternion(*q)

        print start_pose

        print "====== move to position ======="


        # KDL
        # arm.set_joint_value_target(start_pose, True)

        # IK Fast
        arm.set_position_target([start_pose.pose.position.x, start_pose.pose.position.y, start_pose.pose.position.z],
                                arm.get_end_effector_link())

        arm.go()
        rospy.sleep(2)

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == '__main__':
    CobraMove()
