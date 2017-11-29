#!/usr/bin/env python

import numpy as np
import math

def make_linfractrans(a, b, c, d):
    return np.array([[a, b], [c, d]])

def make_point_reflection(x, y):
    return make_linfractrans(y, x, -1, -y)

def make_line_reflection(l1, l2):
    return make_linfractrans(-l2, -l1, 1, l2)

def make_line_reflection_end(l1, l2):
    return make_linfractrans(-1, -l1, 0, 1)

def apply_transformation(matrix, z):
    num = matrix[0][0]*z + matrix[0][1]
    den = matrix[1][0]*z + matrix[1][1]
    if (den == 0):
        return ("infty", "infty")
    return num / den


