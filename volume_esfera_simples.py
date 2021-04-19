# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:57:47 2016

@author: visitante
"""

"Calculando Volume Esfera"

'''
Volume esfera
V= 4/3 *pi * raio**3
'''

#importando de uma bliblioteca externa
from math import pi

raio = 3.0           #metros

volume = (4.0/3.0) * pi * raio**3          #duplo * (**) quer dizer o expoente

print "O Volume da Esfera eh: %f metros cubicos" %(volume)