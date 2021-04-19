# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:16:57 2016

@author: visitante
"""

import matplotlib.pyplot as plt
from mapa_logi import f

x0 = 0.01
r = 2.8
rg = []
xg = []
dr = 0.01
dx = 0.001
N = 900
h = 0.1
for i in range(120):
    x0 = 0.01    
    for n in range(1000):
        t,x = f(r,x0,N,h)        
        rg.append(r)
        xg.append(x[-1]) #x[-1] é o ulimo termo do vetor
        x0 = x0 + dx
    r = r + dr
    
plt.grid(True)    
plt.plot(rg, xg, 'r,')