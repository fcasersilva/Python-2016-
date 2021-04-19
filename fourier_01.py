# -*- coding: utf-8 -*-
"""
SERIES DE FOURIER

"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos

# definindo uma funcao para fazer a soma da serie
def fourier (n,t):
    #bn = 2*((-1)**(n+1))
    return 2*((-1)**(n+1))*sin(n*t)/n
    
t = np.arange(-4.0*np.pi, 4.0*np.pi, 0.01)
tc = np.arange(-np.pi, np.pi, 0.01)

# loop para fazer a soma
def four(N):
    f = 0.0
    for n in range(1,N):
        f += fourier(n,t)
    return f    
    
f = four(2)
#f = four(100)    
plt.plot(t,f)
plt.plot(tc, tc, 'r')
plt.grid(True)
plt.plot([-2.2*np.pi, 2.2*np.pi], [0,0], 'k')
plt.plot([0,0], [-5,5], 'k')