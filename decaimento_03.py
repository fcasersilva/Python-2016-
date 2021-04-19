# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Utilizando o Metodo de Euler para resolver Eq. Diferenciais Ordinairias (EDO)
'''

''' Eq. para descrever o decaimento radioativo de um nucleo qlqr'''

import matplotlib.pyplot as plt
import numpy as np

'''
Resolvendo a EDO
dx/dt = -x**3 + sen(t)
x[n+1] = x[n] + (dx/dt)*t
x[n+1] = x[n] + (-x[n]**3-sen(t[n]))*h
'''

def solve(N):
 #Definindo as cond inicias
    a = 0.0         #t inicial
    b= 10.0         #t final
    h = (b-a)/N     #valor do paaso  
    x0 = 0.0
    t0 = 0.0
    x = [x0]    
    t = [a]
    N = 10
    
    for n in range(N):
        x.append(x[n] + (-x[n]**3 - np.sin(t[n]))*h)
        t.append(t[n]+h)
    plt.plot(t0, x0, '--')
    plt.plot(t0, x0, 'b-')
    
solve (100)
#solve (100000)
#solve (10000)

plt.title ('Decaimento com Metodo de Euler')
plt.xlabel('t(anos)')
plt.ylabel('Num. de Nucleos')
plt.grid(True)









