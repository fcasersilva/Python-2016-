# -*- coding: utf-8 -*-
"""
SISTEMA TERRA - SOL (PG 123 e 124 APOSTILA)

"""
from math import pi, sqrt
import matplotlib.pyplot as plt

def orbita(t0, vx0, x0, vy0, y0, IT, dt):
    r = sqrt(x0**2 + y0**2)
    t = [t0]
    vx = [vx0]
    x = [x0]
    vy = [vy0]
    y = [y0]
    dt = 0.001
    
    for n in range (IT):
        vx.append(vx[n] - ((4*pi*pi*x[n])/r**3)*dt)
        x.append(x[n] + vx[n+1]*dt )
        vy.append(vy[n] - ((4*pi*pi*y[n])/r**3)*dt )
        y.append (y[n] + vy[n+1]*dt )
        t.append (t[n] + dt)
      
   
    plt.plot(x, y)
     plt.xlabel ('x (UA)')
    plt.ylabel ('y (UA)')
    plt.grid(True)
    plt.plot(0.0, 0.0, 'ro') #r = red; o = simbolo (sol)    
    plt.title('Orbita circular do planeta-Sol')

orbita(0.0, 0.0, 1.0, 2*pi, 0.0, 1000, 0.001)