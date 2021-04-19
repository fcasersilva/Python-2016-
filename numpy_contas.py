# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:22:01 2016

@author: visitante
"""

"Fazendo contas"

import numpy as np

t = np.arange (0,100, 0.1)

x = 2.8*np.cos(3.0*t)
#np.algumacoisa evita a necessidade de importar o math e diminiu as iteraçoes

print x

'Salvando dados'

#salva array 1D ou 2d com extensão .npy
np.save ('nome-do-arquivo_t', t)
np.save ('nome-do-arquivo_x', x)

#salva multiplos arrays com varias dimensões com extensão .npz
#salva na pasta onde este arq esta, caso queira outra pasta especif com C:/
np.savez ('nome-do-arquivo', eixo_t = t, eixo_x = x)

#salva como arquivo de texto na extensao desejada
#(usar ".txt" ou ".dat", as demais costumam dar erro)
np.savetxt ('nome-do-arquivo_t.txt', t)
np.savetxt ('nome-do-arquivo_x.txt', x)
#ou
np.savetxt ('nome-do-arquivo_x.txt', (t, x))