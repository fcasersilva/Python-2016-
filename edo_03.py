# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:06:06 2016

@author: visitante
"""

'''
Importanto edo_02 ou um outro programa que
tenha uma função que eu precise/queira usar e ja tenha sido definida
'''

import matplotlip.pyplot as plt
from edo_02 import solve

t,x = solve(50)

plt.plot(t, x)