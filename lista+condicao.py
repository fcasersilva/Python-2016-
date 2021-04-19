# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 10:12:22 2016

@author: visitante
"""

'''Listas com condiçoes - exercicio pg. 69 apostila '''

massa = float(raw_input ("Insira a qnt de peixes em kg:\n"))
                                      # \n passa para linha de baixo

limite = 50.0
multa = 4.00

if massa >= limite:
    multaTotal= (massa - limite) * multa
     
    print 'A multa a ser paga eh de %0.2f reais' %(multaTotal)
    
else:
    print "Fique traquilo. Não tem multa."