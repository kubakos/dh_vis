#!/usr/bin/env python3
from math import radians, sin, cos
import numpy as np


class CoordinateFrame(object):
    # Creates a coordinate frame as a homogeneous matrix

    def __init__(self, base=None):
        # [0,0] - [2,2] rotation
        # [0,3] - [2,3] position
        # [3,0] - [3,2] perspective parameters
        # [3,3] scale factor

        self.matrix = np.identity(4)
        if base != None:
            self.matrix = np.copy(base.get())

    def __getitem__(self, key):
        return self.matrix[key]

    def get(self):
        return self.matrix

    def roll(self, angle_X):
        # Rotates the homogeneous matrix by angle_X by the X axis

        rolled_by = np.identity(4)
        rolled_by[1, 1] = cos(radians(angle_X))
        rolled_by[1, 2] = -(sin(radians(angle_X)))
        rolled_by[2, 1] = sin(radians(angle_X))
        rolled_by[2, 2] = cos(radians(angle_X))

        self.matrix = np.dot(self.matrix, rolled_by)

    def pitch(self, angle_Y):
        # Rotates the homogeneous matrix by angle_Y by the Y axis

        pitched_by = np.identity(4)
        pitched_by[0, 0] = cos(radians(angle_Y))
        pitched_by[0, 2] = sin(radians(angle_Y))
        pitched_by[2, 0] = -(sin(radians(angle_Y)))
        pitched_by[2, 2] = cos(radians(angle_Y))

        self.matrix = np.dot(self.matrix, pitched_by)

    def yaw(self, angle_Z):
        # Rotates the homogeneous matrix by angle_Z by the Z axis

        yawed_by = np.identity(4)
        yawed_by[0, 0] = cos(radians(angle_Z))
        yawed_by[0, 1] = -(sin(radians(angle_Z)))
        yawed_by[1, 0] = sin(radians(angle_Z))
        yawed_by[1, 1] = cos(radians(angle_Z))

        self.matrix = np.dot(self.matrix, yawed_by)

    def set_pos(self, posX, posY, posZ):
        # Sets the position of the homogeneous matrix

        self.matrix[0, 3] = posX
        self.matrix[1, 3] = posY
        self.matrix[1, 3] = posZ

    def set_perspective(self, X, Y, Z):
        # Sets the perspective parameter of the homogeneous matrix

        self.matrix[3, 0] = X
        self.matrix[3, 1] = Y
        self.matrix[3, 2] = Z

    def set_scale(self, scale):
        # Sets the scale parameter of the homogeneous matrix

        self.matrix[3, 3] = scale

    def set_param_a(self, aX, aY):
        # Sets the 'a' parameter of the convention

        self.matrix[0, 3] += aX
        self.matrix[1, 3] += aY

    def set_param_alpha(self, alphaX, alphaY):
        # Sets the 'alpha' parameter of the convention

        self.roll(alphaX)
        self.pitch(alphaY)

    def set_param_d(self, d):
        # Sets the 'd' parameter of the convention

        self.matrix[2, 3] += d

    def set_param_theta(self, theta):
        # Sets the 'theta' parameter of the convention

        self.yaw(theta)
