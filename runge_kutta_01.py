# -*- coding: utf-8 -*-



'''
Metodo Runge-Kutta pra resolver EDO's

Esse metodo divide a curva em 4 partes

x[n+1]= x[n] + (h/6)*(k1 + 2*k2+ 2*k3 + k4)
k1 = f( x[n]            , t[n]) 
k2 = f( x[n] + (h*k1)/2), t[n]+ h/2)
k3 = f( x[n] + (h*k2)/2), t[n]+ h/2)
k4 = f( x[n] + (h*k3), t[n]+ h)

EDO A SER RESOLVIDA:
dx/dt = -x**3 = sen(t)
'''

import matplotlib.pyplot as plt
import numpy as np

def solve_rk4(N):
 # cond iniciais
    a= 0.0
    b = 10.0
    h = (b-a)/N
    x0 = 0.0
 # vetores t e x    
    t = [a]
    x = [x0]
  
 # main loop
    for n in range(N):
         k1 = -(x[n]            )**3 + np.sin(t[n]    )
         k2 = -(x[n]  + (h*k1)/2)**3 + np.sin(t[n]+h/2)
         k3 = -(x[n]  + (h*k2)/2)**3 + np.sin(t[n]+h/2)
         k4 = -(x[n]  + (h*k3)  )**3 + np.sin(t[n]+ h  )
      
         x.append(x[n] + (h/6)*((k1 +2*k2 + 2*k3 + k4)))
         t.append(t[n] +  h) 

    return t,x
    
#comentados para poder usar em runge_kutta_02
#t,x = solve_rk4(100)

#plt.plot(t,x)
#plt.grid(True)
