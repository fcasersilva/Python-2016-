# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"Utilidades do Numpy"

import numpy as np     # adotamos para o exerc np como abrev de numpy

# matrizes e vetores

#criar arays unidimensionais com zeros
a = np.zeros(3)
print a

#criar arays bidimensionais com zeros
b= np.zeros((3,2))
print b

#criar matriz identidade
c = np.eye(5)
print c

#criar arayscom termos = 1
d= np.ones(5)
e= np.ones((2,6))
print d
print e

'Informações de arrays'

print e.shape       # retorna(mostra) o formato
print e.size        # retorna o tamanho
print e.sum()       # retorna a soma dos termos da matriz
f= np.random.randon(4)   #preenche a matriz com num aleatorios

print f
print f.mena()      #retorna a medida dos termos
print f.std()       #retorna desvio padrão