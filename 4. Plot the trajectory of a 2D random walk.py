#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:19:39 2024

@author: brettnakao
"""

import numpy as np

rng = np.random.default_rng(42)

# X-step
x_sample = rng.random(500)
x_step = 2 * (x_sample > .5) - 1
x_coord = np.cumsum(x_step)

# Y-step
y_sample = rng.random(500)
y_step = 2 * (y_sample > .5) - 1
y_coord = np.cumsum(y_step)

# Plot coordinates
import matplotlib.pyplot as plt
plt.plot(x_coord, y_coord)
plt.title('2D Random Walk')
plt.xlabel('x-step')
plt.ylabel('y-step')
plt.axis('equal')
plt.show()