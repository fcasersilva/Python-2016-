# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 10:52:56 2016

@author: visitante
"""

"ESTRUTURAS DE REPETICAO"

'''
PODEMOS USAR O while ou for p/ repetir partes do codigo
'''

from time import sleep

condicao = True

i= 0

while condicao:
    print i
    sleep(1) #sleep da um intervalo em seg entre as interacoes
    i= i+1  #ou i+=1
    
    if i>10:
        condicao= False