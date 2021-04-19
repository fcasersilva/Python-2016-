# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:08:20 2016

@author: visitante
"""

"Criando Arrays"

import numpy as np

#lista tradicional
a = [2.4, 3.5, 1.0]

#cria arrays 1D
b = np.array([2.4, 3.5, 1.0])

#cria arrays 2D
c= np.array ([ [1,2,3] , [4,5,6] ])

#argumentos: inicio, fim, passo (de qto em qto)
d = np.arange(0, 10.1, 0.1)
print d

#argumentos: inicio, fim, comprimento
e = np.linspace(0, 11, 83)
print e

print c [0][1]   # linha, coluna
#ou
print c[0,1]

c[0,1] = 8 # subst um qlqr termo por outro 
print c