#!/usr/bin/env python

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"


class Config:
    def __init__(self, max_gripper, number_of_disks, disk_height, tower_height, tower_positions,
                 tower_variable_height, debug=0):
        self.DEBUG = debug
        self.max_gripper = max_gripper
        if self.DEBUG is 1:
            print "[DEBUG] max_gripper: ", self.max_gripper
        self.number_of_disks = number_of_disks
        if self.DEBUG is 1:
            print "[DEBUG] number_of_disks: ", self.number_of_disks
        self.disk_height = disk_height / 100.0
        if self.DEBUG is 1:
            print "[DEBUG] disk_height: ", self.disk_height / 100.0
        self.tower_height = tower_height
        if self.DEBUG is 1:
            print "[DEBUG] tower_height: ", self.tower_height
        self.tower_positions = tower_positions
        if self.DEBUG is 1:
            print "[DEBUG] tower_positions: ", self.tower_positions
        self.tower_variable_height = tower_variable_height
        if self.DEBUG is 1:
            print "[DEBUG] tower_variable_height: ", self.tower_variable_height

    def get_max_gripper(self):
        return self.max_gripper

    def get_number_of_disks(self):
        return self.number_of_disks

    def get_disk_height(self):
        return self.disk_height

    def get_tower_height(self):
        return self.tower_height

    def get_tower_positions(self):
        return self.tower_positions

    def get_tower_variable_height(self):
        return self.tower_variable_height

    def set_tower_positions(self, positions):
        self.tower_positions = positions
