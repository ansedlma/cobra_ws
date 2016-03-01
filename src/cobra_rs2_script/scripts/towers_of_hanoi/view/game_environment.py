#!/usr/bin/env python

import rospy
from moveit_python import PlanningSceneInterface
from moveit_msgs.msg import PlanningScene

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

REFERENCE_FRAME = 'base_link'


class World:
    def __init__(self, tower_array, disk_array, config, debug=0):
        print "[INFO] Initialise World"
        self.DEBUG = debug
        # initialise arrays
        self.tower_array = tower_array
        self.disk_array = disk_array
        # configs
        self.max_gripper = config.get_max_gripper()
        self.disk_height = config.disk_height
        self.tower_positions = config.tower_positions

        self.planning_scene_interface = PlanningSceneInterface(REFERENCE_FRAME)
        # Create a scene publisher to push changes to the scene
        self.scene_pub = rospy.Publisher('planning_scene', PlanningScene, queue_size=10)

    """Calls a method to display the collision objects.
    """
    def create_planning_scene(self):
        print "[INFO] Create_planning_scene"
        self.display_towers_and_disks()

    """This method collects all needed information and
    publish them to other methods.
    """
    def display_towers_and_disks(self):
        print "[INFO] Display towers and disks"
        for tower in self.tower_array:
            # call method to publish new tower
            self.publish_scene(tower.get_position(), tower)
            # set color by name
            self.planning_scene_interface.setColor(tower.get_name(), 1.0, 1.0, 1.0)
            # publish color
            self.planning_scene_interface.sendColors()
        for disk in self.disk_array:
            self.publish_scene(disk.get_position(), None, disk)
            self.planning_scene_interface.setColor(disk.get_id(), disk.get_color()[0], disk.get_color()[1],
                                                   disk.get_color()[2], disk.get_color()[3])
            self.planning_scene_interface.sendColors()
        # wait for sync after publishing collision objects
        self.planning_scene_interface.waitForSync(5.0)
        rospy.sleep(5)

    """This method creates a box or a cylinder with methods of
    the planning scene interface.
    :param position: the position of the new collision object
    :param tower: the tower object
    :param disk: the disk object
    """
    def publish_scene(self, position, tower=None, disk=None):
        if tower is not None:
            self.planning_scene_interface.addBox(tower.get_name(), self.max_gripper / 100.0, self.max_gripper / 100.0,
                                                 (self.tower_positions[tower.get_id() - 1][2] * 2), position[0],
                                                 position[1], position[2])
        else:
            self.planning_scene_interface.addCylinder(disk.get_id(), self.disk_height, disk.get_diameter() / 2,
                                                      position[0], position[1], position[2])

    """This method cleans the planning scene.
    :param close: with this flag a new planning scene objects will be removed
    in sync otherwise the object will be deleted without syncing the scene
    """
    def clean_up(self, close=False):
        if close:
            # get the actual list after game
            self.planning_scene_interface = PlanningSceneInterface(REFERENCE_FRAME)
        for name in self.planning_scene_interface.getKnownCollisionObjects():
            if self.DEBUG is 1:
                print("[DEBUG] Removing object %s" % name)
            self.planning_scene_interface.removeCollisionObject(name, False)
        for name in self.planning_scene_interface.getKnownAttachedObjects():
            if self.DEBUG is 1:
                print("[DEBUG] Removing attached object %s" % name)
            self.planning_scene_interface.removeAttachedObject(name, False)
        if close:
            self.planning_scene_interface.waitForSync(5.0)
            pass

    """This method corrects the position of the moved disk.
    :param tower: parent tower of the disk
    """
    def refresh_disk_pose(self, tower):
        print "[INFO] Refresh disk pose"
        disk = tower.get_last()
        if self.DEBUG is 1:
            print "[DEBUG] Refresh", disk.get_id(), "pose:", disk.get_position(), "tower size", tower.get_size(),\
                "tower pose", tower.get_position()
        # remove the disk from planning scene
        self.planning_scene_interface.removeCollisionObject(disk.get_id(), False)
        # publish collision object and set old color
        self.publish_scene(disk.get_position(), None, disk)
        self.planning_scene_interface.setColor(disk.get_id(), disk.get_color()[0], disk.get_color()[1],
                                               disk.get_color()[2], disk.get_color()[3])
        self.planning_scene_interface.sendColors()
