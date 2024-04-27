#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:36:27 2024

@author: brettnakao
"""

import numpy as np

def distance(initial_point, final_point = (0, 0), metric = "taxi"):
    """
    

    Parameters
    ----------
    initial_point : (x1, y1)
    tuple, list or array of origin coordinates
    
    final_point : (x2, y2)
    tuple, list or array of final coordinates

    Returns the straightline distance |x1 - x2| + |y1 - y2|
    -------
    None.

    """
    if metric == 'taxi':
        distance = abs(final_point[0] - initial_point[0]) + abs(final_point[1] - initial_point[1])
    else:
        distance = np.sqrt((final_point[0] - initial_point[0])**2 + (final_point[1] - initial_point[1])**2)
    
    return distance

# =============================================================================
# point_A = (0, 0)
# point_B = (3, 5)
# 
# straight_distance = distance(point_A, point_B)
# 
# rate = 1 # rate in dollars per mile
# 
# trip_cost = rate * straight_distance
# =============================================================================