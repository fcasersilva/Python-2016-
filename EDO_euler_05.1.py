# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Resolvendo EDO'

import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,t):
    return x**2 + y**2 -6   #dx/dt = Vx
def f2(x,y,t):
    return x**2 -y    # dy/dt = Vy

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
yCI=np.arange(-3,2.4,0.2)
"colcar o '.' pois estamos trabalhando com numeros reais"  

xy=np.meshgrid (xCI, yCI)
"Cria uma matriz de cada um dos vetores e define isso como pto de inicio"


plt.close('all')
"comando para fechar todos os grafios abertos e nao travar o algoritmo"

for i in range(len(xCI)):
    for j in range(len(yCI)):
        x,y,t = fit(1000,xCI[i],yCI[j])
        Vx = f1 (xCI[i], yCI[j], t)
        Vy = f2 (xCI[i], yCI[j], t)
        plt.quiver(xCI[i],yCI[j], Vx, Vy, linewidth=0.5)
        "quiver mostra a inclinação e a convergencia da curva"        
        plt.plot(x,y)






