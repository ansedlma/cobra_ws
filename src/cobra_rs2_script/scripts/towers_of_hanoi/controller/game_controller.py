#!/usr/bin/env python

import math
from copy import deepcopy
from random import randint
from model.tower_model import Tower
from model.disk_model import Disk
from robot.cobra_robot import Robot

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"


class Controller:
    def __init__(self, config, debug=0):
        print "[INFO] Initialise Controller"
        self.DEBUG = debug

        self.disk_array = None
        self.tower_array = None

        # config
        self.config = config

        self.max_gripper = config.get_max_gripper()
        self.number_of_disks = config.get_number_of_disks()
        self.disk_height = config.disk_height
        self.tower_height = config.tower_height
        self.tower_variable_height = config.get_tower_variable_height()
        self.tower_positions = config.get_tower_positions()
        self.config.set_tower_positions(self.update_tower_position(self.tower_variable_height))
        self.tower_positions = deepcopy(config.tower_positions)

        self.world = None
        self.robot = None
        self.init_objects(config)

    """This method initialise various objects.
    """
    def init_objects(self, config):
        self.disk_array = self.generate_disks()
        self.diameter_of_disks()
        self.set_disk_ids()
        self.tower_array = self.generate_towers()
        self.set_disk_positions(self.disk_array)
        self.orientation_of_towers(1)
        self.tower_array[0].set_disks(self.disk_array)

        # robot
        self.robot = Robot(config, self.DEBUG)

    """This method generates disks.
    :returns: disk array
    """
    def generate_disks(self):
        print "[INFO] Generate Disks"
        if self.DEBUG is 1:
            print "[DEBUG] Disks to create: ", self.number_of_disks
            print "[DEBUG] Generate random Colors"
        disk_array = [None] * self.number_of_disks
        for i in range(0, self.number_of_disks):
            disk_array[i] = Disk(None, None, None, self.DEBUG)
        return disk_array

    """This method corrects the disk positions
    of a tower after the robot places a disc.
    :param rad: yaw orientation
    """
    def update_disk_values(self):
        print "[INFO] Update disk values"
        for tower in self.tower_array:
            self.set_disk_positions(tower.get_disks(), tower.get_id())

    """This method calculates the diameter of the disks
    depending on the max value of the gripper and the number of disks.
    """
    def diameter_of_disks(self):
        print "[INFO] Diameter of disks"
        delta_diameter = self.max_gripper / self.number_of_disks
        for i in range(0, self.number_of_disks):
            self.disk_array[i].set_diameter(round(((self.max_gripper - (i * delta_diameter)) / 100.0), 3))
            if self.DEBUG is 1:
                print "[DEBUG] Generated diameter disk", i + 1, "(for cm * 100): ", self.disk_array[i].get_diameter()

    """This method sets the id number for each disk.
    """
    def set_disk_ids(self):
        print "[INFO] Set disk ids"
        ident = self.number_of_disks
        for i in range(0, self.number_of_disks):
            self.disk_array[i].set_id("disk_id_" + str(ident))
            if self.DEBUG is 1:
                print "[DEBUG]", self.disk_array[i].get_id()
            ident -= 1

    """This method generates the towers.
    :returns: tower array
    """
    def generate_towers(self):
        print "[INFO] Generate towers"
        tower_array = [None] * 3
        for i in range(0, 3):
            tower_array[i] = Tower("tower_id_" + str(i + 1), i + 1, self.orientation_of_towers(i),
                                   self.tower_positions[i])
            if self.DEBUG is 1:
                print "[DEBUG] Tower", i + 1, ":  name:", tower_array[i].get_id(), ", pos:",\
                    tower_array[i].get_position(), ", ori:", tower_array[i].get_rad()

        return tower_array

    """This method calculates the orientation of the towers regarding the base
    of the robot. The further use of the orientation is to adjust the disks to the eef.
    :param index: index of the tower in tower array
    :returns: the angle in rad
    """
    def orientation_of_towers(self, index):
        print "[INFO] Orientation of towers"
        tower_pos_list = self.tower_positions[index]
        return round(math.atan2(tower_pos_list[1], tower_pos_list[0]), 4)

    """This method sets the position for every disk.
    :param disks: the disks array of a tower
    :param tower_num: the tower id
    """
    def set_disk_positions(self, disks, tower_num=1):
        print "[INFO] Disk positions"
        disk_number_offset_mul = 0
        tower_pos_list = deepcopy(self.config.get_tower_positions()[tower_num - 1])
        for disk in disks:
            position = [None] * 3  # x,y,z
            position[0] = tower_pos_list[0]
            position[1] = tower_pos_list[1]
            position[2] = round((tower_pos_list[2] * 2) + (self.disk_height * disk_number_offset_mul) +
                                (self.disk_height / 2), 4)
            disk.set_position(position)
            if self.DEBUG is 1:
                print "[DEBUG] Disk poses:", disk.get_position()
            disk_number_offset_mul += 1

    """This method starts the pick move action on the robot.
    :param tower: the parent tower
    :returns: the attached disk
    """
    def pick(self, tower):
        print "[INFO] Pick move"
        return self.robot.pick_manager.pick(tower)

    """This method calls the pick and the place action.
    :param from_tower: the parent tower
    :param dest_tower: the goal tower
    """
    def pick_and_place(self, from_tower, dest_tower):
        attached_disk = self.pick(from_tower)
        self.place(dest_tower, attached_disk)

    """This method calls the place action of the robot.
    :param tower: the goal tower
    :param disk: the attached disk
    """
    def place(self, tower, disk):
        print "[INFO] Place move"
        self.robot.place_manager.place(tower, disk)
        self.update_disk_values()
        if self.DEBUG is 1:
            for tower in self.tower_array:
                for disk in tower.get_disks():
                    print "[DEBUG] After place: disk_id in tower", tower.get_id(), "is:", disk.get_id(),\
                        "pos:", disk.get_position()

    """This method starts the tower of hanoi algorithm.
    :param world: the world object
    """
    def tower_of_hanoi(self, world):
        print "[INFO] Start tower of hanoi"
        self.world = world
        # move tower with size (num of disks) from tower1 to tower3 with tower2
        self.move_tower(self.tower_array[0].get_size(), self.tower_array[0], self.tower_array[2], self.tower_array[1])

    """This method is a recursive method to solve the algorithm.
    :param height: the number of disks on the tower
    :param from_tower: the source tower
    :param to_tower: the destination tower
    :param with_tower: the help tower
    """
    def move_tower(self, height, from_tower, to_tower, with_tower):
        if height >= 1:
            self.move_tower(height - 1, from_tower, with_tower, to_tower)
            self.move_disk(from_tower, to_tower)
            self.move_tower(height - 1, with_tower, to_tower, from_tower)

    """This method calls the pick and place action and moves a disk.
    After the move this method will refresh the scene.
    :param from_tower: the source tower
    :param to_tower: the destination_tower
    """
    def move_disk(self, from_tower, to_tower):
        print "[INFO] Move disk"
        if self.DEBUG is 1:
            print "[DEBUG] Moving disk", from_tower.get_last().get_id(), " ", "from ",\
                from_tower.get_name(), " to", to_tower.get_name()
        self.pick_and_place(from_tower, to_tower)
        self.refresh_scene(to_tower)

    """This method refreshes the scene and corrects the
    position of the disks on the tower.
    :param tower: the tower with disks
    """
    def refresh_scene(self, tower):
        self.world.refresh_disk_pose(tower)

    """This method calls the defined rest position after the
    algorithm has finished.
    """
    def finish(self):
        self.robot.start_position()

    """This method calculates the new tower positions in case the
    "tower_variable_position"-flag was set to 'True'.
    :param tower_variable_height: flag for variable height
    :returns: new tower positions
    """
    def update_tower_position(self, tower_variable_height):
        print "[INFO] Update tower position"
        if tower_variable_height:
            self.tower_positions[0][2] = self.get_rand_tower_height()
            self.tower_positions[1][2] = self.get_rand_tower_height()
            self.tower_positions[2][2] = self.get_rand_tower_height()
            if self.DEBUG is 1:
                print "[DEBUG] New Tower z-pos: ", self.tower_positions[0][2]
                print "[DEBUG] New Tower z-pos: ", self.tower_positions[1][2]
                print "[DEBUG] New Tower z-pos: ", self.tower_positions[2][2]
            return self.tower_positions
        return self.tower_positions

    """This method returns a random int between -5 and 5.
    :returns: random int
    """
    def get_rand_tower_height(self):
        return round((self.tower_height + (randint(-5, 5) / 100.0)) / 2, 2)
