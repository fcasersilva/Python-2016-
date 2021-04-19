# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Resolvendo EDO'

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,t):
    return -(7./9.)*x -(8./9.)*y
def f2(x,y,t):
    return -(4./9.)*x +(7./9.)*y 

def fit(N,x0,y0):   
    a = 0.0     #t0
    b = 10.0    #tf
    h = (b-a)/N #tamanho do passo
    t = [0.0]
    x = [x0]
    y = [y0]
    
    for n in range(N):
        x.append(x[n] +h*f1(x[n],y[n],t[n]))
        y.append(y[n] +h*f2(x[n],y[n],t[n]))    
        t.append(t[n]+h) 
    return x,y,t

xCI=np.arange(-20.,20.,1.)
yCI=np.arange(-20.,20.,1.)

xy=np.meshgrid (xCI, yCI)

for i in range(len(xCI)):
    for j in range(len(yCI)):
        x,y,t = fit(1000,xCI[i],yCI[j])
        plt.xlim(-20.5,20.5)
        plt.ylim(-20.5,20.5)
        Vx = f1 (xCI[i], yCI[j], t)
        Vy = f2 (xCI[i], yCI[j], t)
        plt.quiver(xCI[i],yCI[j], Vx, Vy)    
        plt.plot(x,y)






