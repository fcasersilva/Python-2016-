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

#definindo uma função

def areaCirculo(raio):
#usar TAB PARA DIZER QUAIS INFORMACOES ESTAO DENTRO DA DEFINICAO

    area = pi * raio**2          #duplo * (**) quer dizer o expoente

    print "A area do circulo de raio %0.1f eh: %0.2f metros quadrados" %(raio,area)
    
areaCirculo(2.5)
#calculando para varios raios
areaCirculo(3.0)
areaCirculo(3.5)
areaCirculo(4.0)