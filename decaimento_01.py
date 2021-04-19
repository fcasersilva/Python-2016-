# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Utilizando o Metodo de Euler para resolver Eq. Diferenciais Ordinairias (EDO)
'''

''' Eq. para descrever o decaimento radioativo de um nucleo qlqr
Na(t) = Na(o)*exp (-t/tauA)
'''

import matplotlib.pyplot as plt
import numpy as np

#Solução analitica
Na0 = 100   #qnt inicial de nucleos
tauA = 5.0  #tempo de meia-vida de umk determindado nucleo

tAnal = np.arange (0.0, 50.0, 0.01)
NaAnal = Na0*np.exp(-tAnal/tauA)
#plt.plot(tAnal, NaAnal)

'''
Resolvendo a EDO
dNa/dt = -Na/tauA
Na[n+1] = Na[n] + (dNa/dt)*t
Na[n+1] = Na[n] + (-Na[n]/tauA[n])*h
'''

a = 0.0    #t inicial
b= 50.0    #t final
N = 100    #num iterações
h = (b-a)/N     #valor do paaso

#Definindo as cond inicias

Na0 = 100
tauA = 5.0
t = [a]
Na = [Na0]

for n in range(N):
    Na.append(Na[n] + (-Na[n]/tauA)*h)
    t.append(t[n]+h)


plt.title ('Decaimento com Metodo de Euler')
plt.xlabel('t(anos)')
plt.ylabel('Num. de Nucleos')
plt.grid(True)
plt.plot(t, Na)
plt.plot(tAnal, NaAnal)








