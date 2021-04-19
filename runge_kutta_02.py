# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:01:38 2016

@author: visitante
"""

from runge_kutta_01 import solve_rk4
from edo_02 import solve
import matplotlib.pyplot as plt

trk, xkr = solve_rk4 (100)
teu, xeu = solve (100)

plt.plot (trk, xkr, 'r')
plt.plot (teu,xeu, 'b')