# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:31:26 2016

@author: ninja
"""

"""
Lorenz Model

dx/dt = sig(y-x)
dy/dt = -xz +rx -y
dz/dt = xy -bz
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz01(sig,r, b, x0, y0, z0, dt, IT):
    x = [x0]
    y = [y0]
    z = [z0]
    t = [0.0]
    for n in range(IT):
        x.append(x[n] + (sig   * (y[n] - x[n]))         *dt)
        y.append(y[n] + (-x[n] * z[n] + r*x[n] - y[n])  *dt)
        z.append(z[n] + (x[n]  * y[n] - b*z[n])         *dt)
        t.append(t[n] + dt)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z, s=1,linewidth=0.05)    
    #plt.plot(x,z)
    plt.title('Modelo de Lorenz')
    plt.grid(True)
    
#lorenz01(10.0, 25.0, 8.0/3.0, 1.0, 0.0, 0.0, 0.001, 100000)    
lorenz01(10.0, 25.0, 8.0/3.0, 1.0, 0.0, 0.0, 0.001, 100000)
