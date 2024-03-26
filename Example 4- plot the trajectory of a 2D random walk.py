#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:19:39 2024

@author: brettnakao
"""

import numpy as np

rng = np.random.default_rng()

# X-step
x_sample = rng.random(500)
x_step = 2 * (x_sample > .5) - 1
x_coord = np.sum(x_step)

# Y-step
y_sample = rng.random(500)
y_step = 2 * (y_sample > .5) - 1
y_coord = np.sum(y_step)