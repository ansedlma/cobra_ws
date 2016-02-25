#! /usr/bin/env python

import random

__author__ = "Andreas Sedlmayer"
__email__ = "andreas.sedlmayer89@gmail.com"

DEBUG = 0


class Disk:
    def __init__(self, ident, position, diameter, debug=0):
        self.DEBUG = debug
        self.id = ident
        self.position = position
        self.color = self.get_random_color()
        self.diameter = diameter

    def get_id(self):
        return self.id

    def set_id(self, ident):
        self.id = ident

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_color(self):
        return self.color

    def get_diameter(self):
        return self.diameter

    def set_diameter(self, diameter):
        self.diameter = diameter

    def get_random_color(self):
        colors = []
        alpha = 1.0
        colors.append(self.rand_number())
        colors.append(self.rand_number())
        colors.append(self.rand_number())
        colors.append(alpha)
        if self.DEBUG is 1:
            print "[DEBUG] Colors rgba: ", colors
        return colors

    @staticmethod
    def rand_number():
        return round(random.uniform(0.0, 1.0), 3)
