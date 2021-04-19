# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 10:33:46 2016

@author: visitante
"""

"NOTAS EM FSC-III"

'''
De 0.0 ate 4.0 E
De 4.1 ate 6.0 D
De 6.1 ate 7.5 C
De 7.6 ate 9.0 B
De 9.1 ate 10.0 A

sendo que indices A, B e C aprovam o aluno
'''

nota1 = float(raw_input('Insira a nota 1 \n'))
nota2 = float(raw_input('Insira a nota 2 \n'))

notas = [nota1, nota2]

media = sum(notas)/len(notas)

indice = ['A', 'B', 'C', 'D', 'E' ]

if media <= 4.0:
    print media, indice[4], 'REPROVADO. SOH LAMENTO'

elif media >6.0 and media <= 7.5:
     print media, indice[3], 'APROVADO.'

elif media >7.54 and media <= 9.0:
     print media, indice[3], 'APROVADO. COM FLOGA'

elif media >9.0 and media <= 10.0:
     print media, indice[3], 'APROVADO. AH VELHA!!!!!'

else:
    print "ERROU!!!!"