# -*- coding: utf-8 -*-
"""
SERIES DE FOURIER
"""

import matplotlib.pyplot as plt
import numpy as np

##################################################################
# função serra em senos (fourier_01)
#def fourier(n,t,l):
#    return 2*((-1)**(n+1))*np.sin(n*t)/n
#l= np.pi
#a0 = 0.0
#t = np.arange(-2.1*l,2.1*l,0.01)
#tc = np.arange(-l,l,0.01)    
##################################################################    

##################################################################
# função serra em cossenos
#def fourier(n,t,l):
#    an = 2*(np.cos(n*np.pi) -1.)/(np.pi*n*n)
#    return an*np.cos(n*t)
#l= np.pi
#a0 = np.pi/2.
#t = np.arange(-5.1*l,5.1*l,0.01)
#tc = np.arange(-l,l,0.01)    
##################################################################    

##################################################################
# função t**2 em cossenos
#def fourier(n,t,l):
#    an = 4*np.cos(n*np.pi)/(n*n)
#    return an*np.cos(n*t)
#l= np.pi
#a0 = np.pi*np.pi/3.
#t = np.arange(-4.1*l,4.1*l,0.01)
#tc = np.arange(-l,l,0.01)    
##################################################################

##################################################################
# função t**2 em senos
#def fourier(n,t,l):
#    bn = (2./np.pi)*((2.-np.pi**2*n**2)*np.cos(n*np.pi) -2.)/n**3
#    return bn*np.sin(n*t)
#l= np.pi
#a0 = 0.0
#t = np.arange(-5.1*l,5.1*l,0.01)
#tc = np.arange(-l,l,0.01)    
##################################################################

##################################################################
# Meia reta com inclinação 1
# nota: iniciando a soma em 0 - for n in range(0,N):
#def fourier(n,t,l):
#    return (l/(((2*n+1)*np.pi)**2)*np.cos((2*n+1)*np.pi*t/l) + (l/(2*(n+1)*np.pi))*((-1)**(n+1) -2)*np.sin((n+1)*np.pi*t/l))       
#l= np.pi/2.
#a0 = (3.*l/8.)
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

##################################################################
# função 2*t +1 , -pi<t<pi
#def fourier(n,t,l):
#    bn = -4*np.cos(n*np.pi)/n
#    return bn*np.sin(n*t)
#l= 2*np.pi
#a0 = 1.
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

##################################################################
# função degrau em senos
#def fourier(n,t,l):
#    bn=(2./(n*np.pi))*(1-np.cos(n*np.pi/2))
#    return bn*np.sin(n*np.pi*t/l)
#l= np.pi
#a0 = 0.
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

##################################################################
# função degrau em cossenos
#def fourier(n,t,l):
#    return (2./((2*n-1)*np.pi))*(np.sin((2*n-1)*np.pi/2))*np.cos((2*n-1)*np.pi*t/l)
#l= np.pi/2
#a0 = 0.5
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

##################################################################
# função degrau: 1 ,-pi<t<0 e 2 ,0<t<pi
#def fourier(n,t,l):
#    bn=(1-np.cos(n*np.pi))/(n*np.pi)
#    return bn*np.sin(n*np.pi*t/l)
#l= 2*np.pi
#a0 = 3./2.
#t = np.arange(-1.1*l,1.1*l,0.01)
##################################################################

##################################################################
# Em um circuito RLC é aplicada uma tensão variável e periódica que segue uma
# função degrau de -E0 até + E0
#def fourier(n,t,l):
#    return (2./((2*n-1)*np.pi))*(np.sin((2*n-1)*np.pi/2))*np.cos((2*n-1)*np.pi*t/l)
#l= np.pi/2
#a0 = 0.0
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

##################################################################
# função |sen(t)| em cossenos
#def fourier(n,t,l):
#    an = (2./np.pi)*(np.cos((n+1)*np.pi) +1.)/(1-(n+1)**2)
#    return an*np.cos((n+1)*t)
#l= np.pi
#a0 = 2./np.pi
#t = np.arange(-2.1*l,2.1*l,0.01)
##################################################################

def four(N):
    f =a0
    for n in range(1,N):
        f += fourier(n,t,l)
    return f
    
f = four(100)
plt.plot(t,f)
plt.grid(True)
plt.plot([-2.2*l,2.2*l],[0,0],'k')
plt.plot([0,0],[-2,4],'k')
#plt.plot(tc,tc, 'r')
   
   