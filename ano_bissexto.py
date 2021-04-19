# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:21:10 2016

@author: Fernando
"""

'''
Ano Bissexto
um ano é bissexto se ele for divisível por 400
ou se ele for divisível por 4 e não por 100
'''

Ano = int(raw_input("Diga o ano: "))

if Ano % 4 == 0 and Ano % 100 != 0 :
    print Ano, "é Bissexto"
else:
    print Ano, "não eh Bissexto"