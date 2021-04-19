# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:25:34 2016

@author: visitante
"""

"PRIMEIRO PROG"
'AINDA O 1o PROG'

'''
usa-se 3 aspas (pode ser simples ou dupla) para inserir comentarios longos
ou # para contarios rapidos ou curtos
nao aparece no prog
'''

'PROG PARA CALCULAR MEDIAS DAS NOTAS'

aluno = 'Caser'                     #inserir noke do aluno

nota1=9.5
nota2=3.7
nota3=5.5
nota4=7.5

soma= nota1 + nota2 + nota3 + nota4          #faz a soma das notas

media= soma/4                                #faz a media das notas

mensagem = 'A nota do ' + aluno + ' eh:'   #prepara uma msg para mostar a media

#print mensagem, media                   #transf em cometario pois nao era mais necessario

# mostra a media do aluno / str(argumento) em string
print mensagem + str(media)

