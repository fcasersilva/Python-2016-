# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:34:26 2016

@author: junior.koch
"""

fim = 500

divisores = []

for i in range(1,fim+1):
    if i % 16 == 0:
        #print 'é dividor'
        divisores.append(i)
    #else:
        #print 'não é divisor'
        
print divisores        