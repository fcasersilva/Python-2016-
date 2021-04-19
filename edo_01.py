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
    x = [x0]    
    t = [a]
        
    for n in range(N):
        x.append(x[n] + (-x[n]**3 - np.sin(t[n]))*h)
        t.append(t[n]+h)
    plt.plot(t, x)
    
solve (100000000)
#solve (30)
#solve (50)
#solve (80)
#solve (100)

plt.grid(True)









