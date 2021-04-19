# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"APRENDENDO A USAR LISTAS"

"""
Listas são variavies que podem guiardar outros tipos de variaveis.
Podem utilizar tipos diferentes e ter tamanhos diversos.
"""

produto = [ 'banana', 'bacon', 'cerveja']

print produto

#caso queira apenas um produto ewspecifico

print produto [2]

preco = []     # criua uma lista vazia

preco.append (3.00)      #append() adicona valor na variavel
preco.append (7.89)
preco.append (20.59)

print produto

'''para alterar o valor de algum termo da lista'''

preco[2] = 15.60

print preco

quantidade = [1.60, 3.0, 2]

precototal = [preco[0]*quantidade[0], preco[1]*quantidade[1], \
              preco[2]*quantidade[2]]

#usamos " \ " qdo a linha esta muioto grande e/ou queremos usar a linha debaixo para o mesmo comando

print precototal
print sum(precototal)

''' para saber se colocamos algum produto numa lista'''

print produto.index('bacon')

print max(preco)   # mostra o maximo valor de preco da lista
print min(preco)   # mostra o manimo valor de preco da lista
print len(quantidade) # mostra o comprimento da lista

