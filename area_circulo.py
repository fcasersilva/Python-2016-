# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:57:47 2016

@author: visitante
"""

"Calculando a area do circulo"

'''
Area do cicurculo
A= pi * raio * raio
'''

#importando de uma bliblioteca externa
from math import pi


raio=2.5           #metros

area = pi * raio**2          #duplo * (**) quer dizer o expoente

print area


print "A area do circulo eh: %0.3f metros quadrados" %(area)
