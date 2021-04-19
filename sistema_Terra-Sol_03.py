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

# dados de outros planetas (fonte: nautilus.fis.uc.pt)
# vleoc de translação
# planeta ------ v(km/s) ------- v(UA/ano)
# Mercurio       47.89            10.89
# Venus          35.03            7.36
# Terra          29.79            6.26
# Marte          24.13            5.07
# Jupiter        13.06            2.75
# Saturno        9.64             2.03
# Urano          6.81             1.43

#Terra  t0, vx0, x0,   vy0,  y0,  IT,   dt
orbita(0.0, 0.0, 1.0, 2*pi, 0.0, 1000, 0.001)

#Marte  t0, vx0, x0,   vy0,   y0,   IT,   dt
orbita(0.0, 0.0, 1.524, 5.07, 0.0, 10000, 0.001)

#Jupiter  t0, vx0,  x0,   vy0,  y0,    IT,    dt
orbita(  0.0, 0.0, 5.203, 2.75, 0.0, 100000, 0.01)

#Saturno t0, vx0, x0,   vy0,  y0,  IT,   dt
orbita( 0.0, 0.0, 9.534, 2.03, 0.0, 1000000, 0.01)

#Urano  t0, vx0, x0,   vy0,  y0,  IT,   dt
orbita(0.0, 0.0, 19.10, 1.43, 0.0, 1000, 0.001)
