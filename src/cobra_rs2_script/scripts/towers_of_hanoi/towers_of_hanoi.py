#! /usr/bin/env python

import moveit_commander
import sys
import rospy
from view.game_environment import World
from controller.game_controller import Controller
from controller.config import Config

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

DEBUG = 0  # debug mode

"""Config and information about the
 Cobra RS2 robot.
"""
# MOVEMENT_RANGE_ROBOT_LEFT = -2.96706 (rad)
# MOVEMENT_RANGE_ROBOT_RIGHT = 2.96706 (rad)

# ROBOT  # should not be changed
MAX_GRIPPER = 8.0  # 8 cm range of gripper

# GAME CONFIGURATIONS
# DISKS
NUMBER_OF_DISKS = 3  # amount of disks
DISK_HEIGHT = 2.5  # cm
# TOWER
TOWER_HEIGHT = 0.2  # 20 cm height

TOWER_POSITION_ONE = [0.3, -.25, TOWER_HEIGHT / 2]
TOWER_POSITION_TWO = [0.3, 0.0, TOWER_HEIGHT / 2]
TOWER_POSITION_THREE = [0.3, 0.3, TOWER_HEIGHT / 2]  # x,y for the 3 towers
TOWER_POSITION = [TOWER_POSITION_ONE, TOWER_POSITION_TWO, TOWER_POSITION_THREE]
DIFFERENT_HEIGHT_OF_TOWERS = True  # generates a random offset between -5 and +5 on TOWER_HEIGHT


def show_tower_of_hanoi():
    print ""
    print "   ...Towers of Hanoi...    "
    print ""
    print "############################"
    print "         COBRA RS2          "
    print ""
    print "   |_|       ||     ||      "
    print "  |___|      ||     ||      "
    print " |_____|_____||_____||_____ "
    print ""
    print "############################"
    print ""


def show_end():
    print ""
    print "     ...End of Game...      "
    print ""
    print "############################"
    print "         COBRA RS2          "
    print ""
    print "    ||     ||      |_|      "
    print "    ||     ||     |___|     "
    print " ___||_____||____|_____|____"
    print ""
    print "############################"
    print ""

if __name__ == '__main__':
    # Moveit! initialise and init node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('cobra_towers_of_hanoi', anonymous=True)

    # welcome screen
    show_tower_of_hanoi()

    config = Config(MAX_GRIPPER, NUMBER_OF_DISKS, DISK_HEIGHT, TOWER_HEIGHT, TOWER_POSITION,
                    DIFFERENT_HEIGHT_OF_TOWERS, DEBUG)

    # configure and initialise objects
    controller = Controller(config, DEBUG)

    # initialise planning scene
    world = World(controller.tower_array, controller.disk_array, config, DEBUG)

    # remove old objects from scene
    world.clean_up()

    # add new objects
    world.create_planning_scene()

    # start the game
    controller.tower_of_hanoi(world)

    # robot rest position
    controller.finish()

    # clean up
    world.clean_up(True)

    # goodbye screen
    show_end()

    # exit
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
