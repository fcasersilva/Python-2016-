# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Resolvendo EDO'

import numpy as np
import matplotlib.pyplot as plt

k = 1.0
mi = 1.0
def f1(x,v,t):   # dv/dt
    return -(k/mi)*x +(1./6)*mi*x**3
def f3(x,v,t):   # dv/dt
    return -(k/mi)*x
def f2(x,v,t):   # dx/dt
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
        t.append(t[n]+h) 
    return x,v,t

    for n in range(N):
        v.append(v[n] +h*f3(x[n],v[n],t[n]))
        x.append(x[n] +h*f2(x[n],v[n+1],t[n]))    
        t.append(t[n]+h) 
    return x,v,t

x,v,t = fit(10000,1.0,0.0)
#x2,v2,t2 = fit(1000,1.0,0.0)
plt.plot(x,v)
#plt.plot(x2,v2)





