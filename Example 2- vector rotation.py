#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:22:51 2024

@author: brettnakao
"""

import numpy as np
def rotate(vector, theta):
    """

    Parameters
    ----------
    vector : tuple containing the initial coordinates (x, y)
    theta : angle of rotation in degrees

    Returns
    -------
    rotated_vector: tuple containing the rotated coordinates

    """
    theta_radians = np.radians(theta) # Convert from degrees to radians
    
    rotation_matrix = np.array([[np.cos(theta_radians), -np.sin(theta_radians)], [np.sin(theta_radians), np.cos(theta_radians)]])
    
    rotated_vector = np.dot(rotation_matrix, vector)
    
    return rotated_vector

vec = [1, 0]
theta = 90

r = rotate(vec, theta)

x, y = rotate(vec, theta)

# =============================================================================
# import numpy as np
# def decompose(r, theta):
#     """
#     
# 
#     Parameters
#     ----------
#     r : a float, the length of the vector
#     theta : the angle with the x-axis in radians
# 
#     Returns
#     -------
#     (r_x, r_y), a tuple containing the components of r along x and y
# 
#     """
#     r_y = r * np.sin(theta)
#     r_x = r * np.cos(theta)
#     r_vector = (r_x, r_y)
#     
#     return r_vector
# 
# 
# r_x, r_y = decompose(1, np.pi/2)
# =============================================================================