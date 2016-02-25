#! /usr/bin/env python

import rospy
from moveit_commander import MoveGroupCommander
from robot.movement.move_pick import PickManager
from robot.movement.move_place import PlaceManager
from moveit_python import PickPlaceInterface

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

START_POSITION = "start_position"
ARM_GROUP = "arm"
GRIPPER_GROUP = "gripper"


class Robot:
    def __init__(self, config, debug=0):
        print "[INFO] Initialise Robot"
        self.DEBUG = debug
        # configuration
        self.config = config
        # initialise move groups
        self.arm = MoveGroupCommander(ARM_GROUP)
        self.gripper = MoveGroupCommander(GRIPPER_GROUP)
        # initialise pick and place manager
        if self.DEBUG is 1:
            # verbose mode
            self.pick_and_place = PickPlaceInterface(ARM_GROUP, GRIPPER_GROUP, False, True)
        else:
            # non verbose mode
            self.pick_and_place = PickPlaceInterface(ARM_GROUP, GRIPPER_GROUP, False, False)

        # tolerance: position (in m), orientation (in rad)
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)

        self.place_manager = None
        self.pick_manager = None

        self.initialise_move_actions()
        self.start_position()

    """Initialise the place and pick manager.
    """
    def initialise_move_actions(self):
        self.place_manager = PlaceManager(self.arm, self.pick_and_place, self.config, self.DEBUG)
        self.pick_manager = PickManager(self.arm, self.pick_and_place, self.DEBUG)

    """Move robot arm to "start position".
    """
    def start_position(self):
        self.arm.set_named_target(START_POSITION)
        self.arm.go()
        rospy.sleep(2)
