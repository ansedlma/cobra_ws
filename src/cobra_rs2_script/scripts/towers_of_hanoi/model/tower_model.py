#! /usr/bin/env python

import copy

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"


class Tower:
    def __init__(self, name, ident, orientation, position):
        self.name = name
        self.id = ident
        self.rad = orientation
        self.position = position
        self.disks = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, ident):
        self.id = ident

    def get_rad(self):
        return self.rad

    def set_rad(self, rad):
        self.rad = rad

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def pop(self):
        if self.get_size() > 0:
            return self.disks.pop()
        return None

    def put(self, disk):
        self.disks.append(disk)

    def set_disks(self, disk_array):
        self.disks = copy.deepcopy(disk_array)

    def get_disks(self):
        return self.disks

    def get_size(self):
        return len(self.disks)

    def get_last(self):
        if len(self.disks) > 0:
            return self.disks[len(self.disks) - 1]
        else:
            return None
