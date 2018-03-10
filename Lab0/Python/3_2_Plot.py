# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:57:16 2018

@author: Frederic Freundler
"""

from __future__ import print_function  # Only necessary in Python 2

import biolog  # import biolog for log messages
import numpy as np  # Import numpy as np
from matplotlib import pyplot as plt  # Import pyplot from matplotlib

# Create a numpy array of 100 points between -10 and 10
x = np.linspace(0, 2, 100)
biolog.info(x)
y = np.sin(x-2)*np.exp(-(np.power(x,2))) # Compute the exponential of x

# Plotting the function y
# Create a new figure window
plt.figure()
# Plot x and y
plt.plot(x, y, label='$y = sin(x-2)e^{-x^2}$')
# Turn on grid
plt.grid('on')
# X axis label
plt.xlabel('X-axis')
# Y axis label
plt.ylabel('Y-axis')
# Title of the plot
plt.title('Plotting an exponential function')
# Legend of the plot
plt.legend()
# Show the figure
plt.show()