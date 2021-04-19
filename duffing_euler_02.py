# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Pendulo'

import numpy as np
import matplotlib.pyplot as plt

g = 1.0
l = 1.0

def f1(x,v,t):  #dv/dt
    return -np.sin(x)

def f2(x,v,t):  #dx/dt
    return v


def fit(N,x0,v0):   
    a = 0.0     #t0
    b = 50.0    #tf
    h = (b-a)/N #tamanho do passo
    t = [0.0]
    x = [x0]
    v = [v0]
    
    for n in range(N):
        v.append(v[n] +h*f1(x[n],v[n],t[n]))
        x.append(x[n] +h*f2(x[n],v[n],t[n]))
        # Metodo de Euler        
        #x.append(x[n] +h*f2(x[n],v[n+1],t[n]))        
        # Metodo de Euler-Cromer                
        t.append(t[n]+h) 
    return x,v,t

plt.grid(True)

x,v,t = fit(10000, 1.0, 0.0)
plt.plot(x, v)

x,v,t = fit(10000, 1.0, 0.0)
plt.plot(x, v)

x,v,t = fit(10000, 1.0, 0.0)
plt.plot(x, v)




