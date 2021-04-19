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
'''definindo N como uma variavel pra mnelhorar a visualização do grafico'''

def decay(N):
    a = 0.0    #t inicial
    b= 50.0    #t final
    #N = 100    #num iterações
    h = (b-a)/N     #valor do paaso

    #Definindo as cond inicias
    
    Na0 = 100
    tauA = 5.0
    t = [a]
    Na = [Na0]
    
    for n in range(N):
        Na.append(Na[n] + (-Na[n]/tauA)*h)
        t.append(t[n]+h)
    plt.plot(t, Na, '--')
    plt.plot(tAnal, NaAnal, 'b-')
    
decay (1000)
#decay (1000000)
#decay (10000)


plt.plot([0.0, 50.0], [20.0, 20.0], 'r') #fazendo uma linha para marcar alguma coisa
plt.text(35, 40, 'Safe Line')
# os num 35, 40 eh a posição do texto (eu defino)
plt.arrow(36.5, 39, 0, -15, head_length = 1.5, head_width = 1.0, fc ='k')
# pos. x e y da seta; deslocamento da seta (da onde ate aonde);
#tam da cabeça lagura e preenchimento da cabeça do vetor
plt.title ('Decaimento com Metodo de Euler')
plt.xlabel('t (anos)')
plt.ylabel('Num. de Nucleos')
plt.grid(True)









