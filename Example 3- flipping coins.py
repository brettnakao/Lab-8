#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:00:25 2024

@author: brettnakao
"""

# =============================================================================
# import numpy as np
# 
# rng = np.random.default_rng(seed = 42) # Random number generator object
# 
# rand = rng.random(10) # Generate numbers between 0 and 1
# =============================================================================

import numpy as np

rng = np.random.default_rng()

samples = rng.random(100) # Generates 100 random numbers

flips = (samples > .5)

heads = np.sum(flips)