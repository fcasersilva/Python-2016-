# -*- coding: utf-8 -*-


'''
Utilizando o Metodo de Euler para resolver Eq. Diferenciais Ordinairias (EDO)


Eq. para descrever o decaimento radioativo de um nucleo qlqr
Na(t) = Na(o)*exp (-t/tauA)

Resolvendo a EDO
dNa/dt = -Na/tauA
Na[n+1] = Na[n] + (dNa/dt)*t
Na[n+1] = Na[n] + (-Na[n]/tauA[n])*h
dNb/dt = -Nb/tauB + Na/tauA
Nb[n+1] = Nb[n] + (-Nb[n]/tauB)+Na[n]/tauA)*h

'''

import matplotlib.pyplot as plt

#definindo N como uma variavel pra melhorar a visualização do grafico

def decay(N):
    a = 0.0        #t inicial
    b = 100.0       #t final
    h = (b-a)/N    #valor do paaso

    #Definindo as cond inicias
    
    Na0 = 100
    Nb0 = 0
    tauA = 8.0
    tauB = 4.0
    t = [a]
    Na = [Na0]
    Nb = [Nb0]
    Nt = [0.0]
        
    for n in range(N):
        Na.append(Na[n] + (-Na[n]/tauA)*h)
        Nb.append(Nb[n] + ((-Nb[n]/tauB)+Na[n]/tauA)*h)
        Nt.append(Na[n] + Nb[n])
        t.append(t[n]+h)
    plt.plot(t, Na, 'r-', t, Nb, 'b-')
    plt.plot(t, Nt, 'g-')
    
decay (1000)
#decay (1000000)
#decay (10000)


plt.plot([0.0, 100.0], [20.0, 20.0], 'r--') #fazendo uma linha para marcar alguma coisa
plt.text(35, 40, 'Safe Line')
# os num 35, 40 eh a posição do texto (eu defino)
plt.arrow(36.5, 39, 0, -15, head_length = 1.5, head_width = 1.0, fc ='k')
# pos. x e y da seta; deslocamento da seta (da onde ate aonde);
#tam da cabeça lagura e preenchimento da cabeça do vetor
plt.title ('Decaimento com Metodo de Euler')
plt.xlabel('t (anos)')
plt.ylabel('Num. de Nucleos')
plt.grid(True)









