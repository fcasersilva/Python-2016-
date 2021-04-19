# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:57:47 2016

@author: visitante
"""

"Calculando Volume Esfera para diferentes raios"

'''
Volume esfera
V= 4/3 *pi * raio**3
'''

#importando de uma bliblioteca externa
from math import pi

def volEsfera(raio):
    
    volume = (4.0/3.0) * pi * raio**3          #metros cubicos

    print "O Volume da Esfera de raio %0.2f eh: %0.2f metros cubicos" %(raio,volume)

volEsfera(1.0)
volEsfera(2.0)
volEsfera(4.0)
volEsfera(5.0)