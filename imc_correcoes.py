# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 13:40:51 2016

@author: junior.koch
"""


while True:
    massa  = float(raw_input('Insira a massa. Digite 0 para encerrar.\n'))
    altura = float(raw_input('Insira a altura. Digite 0 para encerrar.\n'))
    
    if massa == 0 or altura == 0:
        print 'Progama encerrado!'
        break
    
    imc = massa/altura**2
    
    print 'O IMC é: %0.1f. Obrigado' %(imc)