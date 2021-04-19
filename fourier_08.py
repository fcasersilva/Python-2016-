# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:41:57 2016

@author: junior.koch


Este código calcula e aproxima funções periódicas em séries de Fourier
É possível escolher apenas entre funções pares ou ímpares

A função de integração utilizada é quadrature vinda do scipy.integrate

"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, cos, sin
from scipy.integrate import quad # integration by intgrature
from scipy.integrate import quadrature as intg

###############################################################################
# Para a função t de 0 até pi em senos ou cossenos
#def f1(t,n):
#    return t
#def f2(t,n):
#    return t*cos(n*t)
#def f3(t,n):
#    return t*sin(n*t)
#
## cada função deve ser analisada separadamente e as condições abaixo devem ser
## modificados conforme a característica de cada uma.
## definições:
#linf = 0.0 #lim inferior
#lsup = pi  #lim superior
#l = pi
#t = np.arange(-2.1*l, 2.1*l, 0.001)    

###############################################################################
    
###############################################################################
# Para a função 1 de 0 até pi em senos ou cossenos
#def f1(t,n):
#    return 1.
#def f2(t,n):
#    return 1.*cos(n*t)
#def f3(t,n):
#    return 1.*sin(n*t)
## definições:
#linf = 0.0 #lim inferior
#lsup = 3*pi/2  #lim superior
#l = pi
#t = np.arange(-4.1*l, 4.1*l, 0.001)    
############################################################################### 
    
###############################################################################
# Para a função t**2 de 0 até 1 em senos ou cossenos
#def f1(t,n):
#    return t**2
#def f2(t,n):
#    return (t**2)*cos(n*t)
#def f3(t,n):
#    return (t**2)*sin(n*t)
# definições:
#linf = 0.0 #lim inferior
#lsup = pi  #lim superior
#l = pi
#t = np.arange(-4.1*l, 4.1*l, 0.001)
###############################################################################

###############################################################################
# Para a função 2*t +1 de 0 até pi em senos ou cossenos
#def f1(t,n):
#    return (2.*t +1.)
#def f2(t,n):
#    return (2.*t +1.)*cos(n*t)
#def f3(t,n):
#    return (2.*t +1.)*sin(n*t)
# definições:
#linf = 0.0 #lim inferior
#lsup = pi  #lim superior
#l = pi
#t = np.arange(-4.1*l, 4.1*l, 0.001)
###############################################################################     

###############################################################################
# Para a função t , 0<t<pi/2 e pi-t , pi/2<t<pi
def f1(t,n):
    return t
def f2(t,n):
    return t*cos(n*t)
def f3(t,n):
    return t*sin(n*t)
# definições:
linf = 0.0 #lim inferior
lsup = pi  #lim superior
l = 3*pi/7
t = np.arange(-4.1*l, 4.1*l, 0.001)
###############################################################################
    
###############################################################################
# Para a função |sin(t)|, onda completa ou meia onda
#def f1(t,n):
#    return abs(sin(t))
#def f2(t,n):
#    return abs(sin(t))*cos(n*t)
#def f3(t,n):
#    return abs(sin(t))*sin(n*t)
###############################################################################

###############################################################################
# funções que calculam a0, an e bn    
def a0(t,l):
    a0 = (2./l)*intg(f1, linf, lsup, maxiter=(1000), args=(l))[0]  
    return a0
def an(t,n,l):
    an = (2./l)*intg(f2, linf, lsup, maxiter=(10000), args=(n))[0]
    return an
def bn(t,n,l):
    bn = (2./l)*intg(f3, linf, lsup, maxiter=(10000), args=(n))[0]
    return bn 
###############################################################################


###############################################################################
# escolha entre função apenas de senos ou apenas de cossenos
# apenas um deve ser True ou todos False
fsin=False         #True para uma série apenas de senos
fcos=True        #True para uma série apenas de cossenos
desloc=False       #True se a0 for claramente zero
###############################################################################

###############################################################################
def four(N):
    if desloc ==False:
        f =a0(t,l)/2.
    else: f = 0.0
    for n in range(1,N):
        if fsin == False:
           feven = an(t,n,l) #an (even = par)
        else: feven =0.0     #an   
        if fcos == False:
            fodd = bn(t,n,l) #bn (odd = impar)
        else: fodd = 0.0     #bn   
        f += feven*cos(n*t) + fodd*sin(n*t)
    return f    
f = four(100)
plt.plot(t,f)
plt.grid(True)
plt.plot([-2.2*l,2.2*l],[0,0],'k')
plt.plot([0,0],[-4,5],'k')
###############################################################################