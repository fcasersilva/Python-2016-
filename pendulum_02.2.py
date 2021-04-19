# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:06:14 2016

@author: ninja
"""

'Resolvendo EDO'

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


def f1(o,w,t,p,q,F0,wd):   # dw/dt
    return -(p**2)*np.sin(o) -q*w + F0*np.sin(wd*t)
def f2(o,w,t):   # do/dt
    return w

def fit(N,o0,w0,p,q,F0,wd):   
    a = 0.0     #t0
    b = 2000.0    #tf
    h = (b-a)/N #tamanho do passo
    t = [0.0]
    o = [o0]
    w = [w0]
    
    for n in range(N):
        if o[n]> 2*np.pi:
            o[n]= o[n]-2*np.pi
        if o[n]< -np.pi:
            o[n]=o[n]+2*np.pi
        w.append(w[n] +h*f1(o[n],w[n],t[n],p,q,F0,wd))
        o.append(o[n] +h*f2(o[n],w[n+1],t[n]))    
        t.append(t[n]+h) 
    return o,w,t
plt.grid(True)

       #fit(    N,  o0, w0,  p,   q, F0, wd)
o1,w1,t = fit(10000,0.2 ,0.0,1.,0.5,1.2,2./3.)
#o2,w2,t = fit(10000,0.201,0.0,1.,0.5,3.3,2./3.)
#plt.plot(t,o1,'r,')
#plt.plot(t,o2,'b')

'Exponte de Lyapunov'
#do = []   # "delta teta" - vetor pra armazenar a dif dos vetores o1 e o2
#for i in range(len(o1)):
#    do.append(abs(o2[i]-o1[i]))     #abs = absoluto (modulo)
#    
#plt.plot(t,do) #plotando a dif das posicoes com o tempo
#plt.yscale('log')   

'Mapa de Poincare (mapa estroboscaopico)'
wp = []
op = []
tp = []

for n in range(len(t)):
    if np.sin(2.*t[n]/3) >= 0.999:
   #queremos o grafico qdo sen = 1 como sao num reais deixamos um valor aprox
   #qto maior a precisao menos pts terá
        wp.append(w1[n])
        op.append(o1[n])
        tp.append(t[n])
plt.grid(True)
plt.plot(op, wp, 'r.')


#oCI=np.arange(-.2,.2,.05)
#wCI=np.arange(-.1,.1,.01)
#
#for i in range(len(oCI)):
#    for j in range(len(wCI)):
#        o,w,t = fit(10000,oCI[i],wCI[j],1.,0.5,1.2,2./3.)
#        plt.plot(o[0],w[0],'b.')
#        plt.plot(o[-1],w[-1],'r.')




