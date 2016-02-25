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
        rospy.init_node('cobra_test_position', anonymous=True)

        arm = MoveGroupCommander(ARM_GROUP)

        arm.allow_replanning(True)

        # max planning time
        arm.set_planning_time(10)
        # start pose
        arm.set_start_state_to_current_state()

        end_effector = arm.get_end_effector_link()
        rospy.sleep(1)

        print "======== create 100 new goal position ========"

        start_pose = PoseStamped()
        start_pose.header.frame_id = arm.get_planning_frame()
        i = 1
        while i <= 1000:
            # random position
            start_pose = arm.get_random_pose(end_effector)
            q = quaternion_from_euler(0.0, 0.0, 0.0)
            start_pose.pose.orientation = Quaternion(*q)

            print "====== move to position", i, "======="

            # KDL
            arm.set_joint_value_target(start_pose, True)
            # IK Fast
            # arm.set_position_target([start_pose.pose.position.x, start_pose.pose.position.y,
            #                         start_pose.pose.position.z], end_effector)

            i += 1
            arm.go()
            rospy.sleep(2)

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == '__main__':
    CobraMove()
