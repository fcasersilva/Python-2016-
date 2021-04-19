# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:47:03 2016

@author: visitante
"""

'''
Mapa Logistico - Diagrma de Bifurcação
x[n+1] = r * x[n]*(1-x[n])
0 <= x <= 1
0 <= r <= 4 # r = tx de cresc
'''

import numpy as np
import matplotlib.pyplot as plt

def f(r, x0, N, h):
    x=[x0]
    t=[0.0]
    for n in range(N):
        x.append(r*x[n]*(1.-x[n]))
        t.append(t[n]+ h)
    return t,x    
    
##cond iniciais
##a) x0 = 0.5 e r = 0.1; r = 0.5; r = 0.9 e N = 30
#t,x = f(0.1, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(0.5, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(0.9, 0.5, 30)    
#plt.plot(t,x, '.')
#
##b) x0 = 0.5 e r = 1.5; r = 2.0; r = 2.9 e N = 30    
#t,x = f(1.5, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(2.0, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(2.9, 0.5, 30)    
#plt.plot(t,x, '.')
#
##c) x0 = 0.5 e r = 3.1; r = 3.2; r = 3.3 e N = 30    
#t,x = f(3.1, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(3.2, 0.5, 30)    
#plt.plot(t,x, '.')
#t,x = f(3.3, 0.5, 30)    
#plt.plot(t,x, '.')