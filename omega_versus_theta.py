# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:22:10 2016

@author: visitante
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.load('omega_fourier.npy')
y = np.load('theta_fourier.npy')

plt.plot(y, x, 'b.')
plt.grid(True)