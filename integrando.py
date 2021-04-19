# -*- coding: utf-8 -*-
"""
INTEGRANDO EM PYTHON
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos
from scipy.integrate import quad
from scipy.integrate import quadrature as intg

# Exemplos Simples

def integrando(x, a, b):
    # x é a variveçl de integracao e a, b sao demais variaveis que aparecem na funcao      
    return a *x + b
# definindo os valores para a e b
a = 2
b = 1
I = quad(integrando, 0, 1, args=(a,b))[0]
   #(funcao a ser integrada, limite inf, limite sup, argumentos)[posicao do termo do vetor]
    #a integral retorna um vetor com o resulyado e o erro. Como nao interessa o erro colocamos [0] no final
print I   

#
#def integrando(x ,a, b):
#    return a * x + b
## definindo os valores para a e b
#a = 2
#b = 1
#I = intg(integrando, 0, 1, maxiter=(60), args=(a,b))[0]
#print I