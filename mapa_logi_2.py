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

def f(r, x0, N):
    x=[x0]
    t=[0.0]
    h = 0.1
    for n in range(N):
        x.append(r*x[n]*(1.-x[n]))
        t.append(t[n]+ h)
    return t,x    

#verificando a estabilidade para 2 cond iniciais

##a) r = 2.9 e x0 = 0.5 e x0 = 0.5001 com N = 300
#t,x = f(2.9, 0.5, 300)    
#plt.plot(t,x, '.')
#t,x = f(2.9, 0.5001, 300)    
#plt.plot(t,x, '.')
#
##b) indo mais alem r = 3.7 e x0 = 0.5 e x0 = 0.5001 com N = 900
#t,x = f(3.7, 0.5, 900)    
#plt.plot(t,x, '.')
#t,x = f(3.7, 0.5001, 900)    
#plt.plot(t,x, '.')
## resultado caotico

##c) r = 3.6 e x0 = 0.5 e x0 = 0.5001 com N = 900
#t,x = f(3.6, 0.5, 900)    
#plt.plot(t,x, '.')
#t,x = f(3.6, 0.5001, 900)    
#plt.plot(t,x, '.')

#d) r = 4. e x0 = 0.5 e x0 = 0.5001 com N = 900
t,x = f(4., 0.5, 900)    
plt.plot(t,x, '.')
t,x = f(4., 0.5001, 900)    
plt.plot(t,x, '.')