# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:35:13 2016

@author: junior.koch
"""

'gráfico em coordenada polar'

import numpy as np
import matplotlib.pyplot as plt


# definindo theta
theta = np.arange(0,2*np.pi,0.001)
# definindo r
r =  1.0 + np.cos(35*theta)

# gráfico
plt.subplot(111, projection='polar')
plt.plot(theta, r, color='r', linewidth=3)
plt.grid(True)