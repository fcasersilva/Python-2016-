# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:41:02 2016

@author: visitante
"""

"Lendo Arquivos e fazendo Gráficos"

import numpy as np
import matplotlib.pyplot as plt #pode usar outro nome mas esse eh mais comum

# Lê o arquivo com extensao .npy
t = np.load('nome-do-arquivo_t.npy')

# print t se eu quiser verificar que eh o arquivo q eu quero

# Lê o arquivo com extensao .npy e .npz
t = np.load ('nome-do-arquivo_t.npy')
x1 = np.load ('nome-do-arquivo_x.npy')
x2 = 2.8*np.cos(3.0*t)
print t
print "\n" #ou só print
print x1

#plota o grafico em 2 fig diferentes
plt.figure(1)
plt.subplot(211) #o termo entre parenteses define a posição que o grafico aparece"
plt.plot(t,x1, 'r--')    # a letra e os simbolos definem a cor e o tipo de linha
plt.xlim(0.0, 10.0)
plt.ylabel ('Amplitude (m)')
plt.grid (True)

plt.subplot(212)
plt.plot(t,x2, 'b-.')
plt.xlim(0.0, 10.0)
plt.xlabel ('Tempo (s)')
plt.grid(True)