# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 10:52:56 2016

@author: visitante
"""

"ESTRUTURAS DE REPETICAO"

'''
PODEMOS USAR O while ou for p/ repetir partes do codigo
'''

from time import time

condicao = True

inicio = time()

i= 0

while condicao:
    print i
    i= i+1  #ou i+=1
    
    if i>1000000:
        condicao= False
        print "Tempo = " , time() - inicio
        #usamos isso para saber qto tempo esta levando pra rodar o prog
        
