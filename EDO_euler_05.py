# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Resolvendo EDO'

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,t):
    return x**2 + y**2 -6
def f2(x,y,t):
    return x**2 -y

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

xCI=np.arange(-5.,1.4,0.2)
yCI=np.arange(-3.,2.4,0.2)


for i in range(len(xCI)):
    for j in range(len(yCI)):
        x,y,t = fit(1000,xCI[i],yCI[j])
        plt.plot(x,y)






