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
        rospy.init_node('cobra_test_cartesian', anonymous=True)

        arm = MoveGroupCommander(ARM_GROUP)

        arm.allow_replanning(True)

        rospy.sleep(2)

        pose = PoseStamped().pose

        # same orientation for all
        q = quaternion_from_euler(0.0, 0.0, 0.0)  # roll, pitch, yaw
        pose.orientation = Quaternion(*q)

        i = 1
        while i <= 10:
            waypoints = list()
            j = 1
            while j <= 5:
                # random pose
                rand_pose = arm.get_random_pose(arm.get_end_effector_link())
                pose.position.x = rand_pose.pose.position.x
                pose.position.y = rand_pose.pose.position.y
                pose.position.z = rand_pose.pose.position.z
                waypoints.append(copy.deepcopy(pose))
                j += 1

            (plan, fraction) = arm.compute_cartesian_path(
                                      waypoints,   # waypoints to follow
                                      0.01,        # eef_step
                                      0.0)         # jump_threshold

            print "====== waypoints created ======="
            # print waypoints

            # ======= show cartesian path ====== #
            arm.go()
            rospy.sleep(10)
            i += 1

        print "========= end ========="

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__=='__main__':
    CobraMove()
