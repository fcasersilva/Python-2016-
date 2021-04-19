# -*- coding: utf-8 -*-
"""
Created on Mon May 09 16:02:55 2016

@author: ninja
"""

"""
Problema de três corpos - Sol, terra e jupiter
"""
from math import pi, sqrt
import matplotlib.pyplot as plt


def orbita(xe0, xj0, IT, dt, ve0, vj0, Ms, Mj, Me): # e = earth
    GMs = 4*pi*pi
    GMj = 4*pi*pi*Mj/Ms
    GMe = 4*pi*pi*Me/Ms    
    t = [0.0]
    #Dados da terra
    vex = [0.0]
    xe = [xe0]
    vey = [ve0]
    ye = [0.0]
    #Dados de jupiter
    vjx = [0.0]
    xj = [xj0]
    vjy = [vj0]
    yj = [0.0001]
#    rej = 0.0
#    r = 0.00
#    rj = 0.0

    for n in range(IT):
        # distancia terra-sol
        #r = sqrt(xe[n]**2 + ye[n]**2)
        #distancia terra jupiter
        #rej = sqrt((xe[n]-xj[n])**2 + (ye[n] - yj[n])**2)
        #distancia sol-jupiter        
        #rj = sqrt(xj[n]**2 + yj[n]**2)
        
        #Movimento da terra
        vex.append(vex[n] + ((-GMs*xe[n])/((sqrt(xe[n]**2+ye[n]**2))**3.0))*dt \
        +((-GMj*(xe[n]-xj[n]))/(sqrt((xe[n]-xj[n])**2 + (ye[n] - yj[n])**2))**3.0)*dt)
    
        xe.append(xe[n]+vex[n+1]*dt)
        
        vey.append(vey[n] + ((-GMs*ye[n])/((sqrt(xe[n]**2+ye[n]**2))**3.0))*dt\
        +((-GMj*(ye[n]-yj[n]))/(sqrt((xe[n]-xj[n])**2 + (ye[n] - yj[n])**2))**3.0)*dt)
        
        ye.append(ye[n]+vey[n+1]*dt)
        
        #Movimento de jupiter
        vjx.append(vjx[n] + ((-GMs*xj[n])/((sqrt(xj[n]**2+yj[n]**2))**3.0))*dt\
        +((-GMe*(xj[n]-xe[n]))/(sqrt((xe[n]-xj[n])**2 + (ye[n] - yj[n])**2))**3.0)*dt)
        
        xj.append(xj[n]+vjx[n+1]*dt)
        
        vjy.append(vjy[n] + ((-GMs*yj[n])/((sqrt(xj[n]**2+yj[n]**2))**3.0))*dt\
        +((-GMe*(yj[n]-ye[n]))/(sqrt((xe[n]-xj[n])**2 + (ye[n] - yj[n])**2))**3.0)*dt)
        
        yj.append(yj[n]+vjy[n+1]*dt)        
        
        # tempo
        t.append(t[n]+dt)
        
#        if y[n] > 0 and y[n-1] < 0:
#            T = t[n-1]
#            break
               
    plt.plot(xe,ye)
    plt.plot(xj,yj)
    plt.plot(0,0, 'ro')
    plt.plot(xe0,0, 'go')
    plt.xlabel('x(UA)')
    plt.ylabel('y(UA)')
    plt.title('Orbita da Terra e Jupiter ao redor do Sol')
    plt.grid(True)


#orbita( xe0,   xj0,     IT,    dt,  ve0,  vj0,     Ms,     Mj,     Me)
#orbita(1.000, 5.203, 100000, 0.001, 6.26, 2.75, 2.0E30, 1.9E27, 6.0E24)
orbita(1.000, 5.203, 100000, 0.001, 6.26, 2.75, 2.0E30, 1.9E27, 6.0E24)

# utilizando os dados do site: nautilus.fis.uc.pt
# as velocidades de translacao dos planetas sao:
#planeta = v(km/s) = v(ua/ano) ==> fator v0 do algoritmo
#merurio = 47,89 = 10.07 ==> 1.602
#venus = 35,03 = 7.36 ==> 1.171
#terra = 29,79 = 6.26 ==> 0.996
#marte = 24,13 = 5.07 ==> 0.807
#jupiter = 13,06 = 2.75 ==> 0.438
#saturno = 9,64 = 2.03 ==> 0.323
#urano = 6,81 = 1.43 ==> 0.228
#netuno = 5,43 = 1.14 ==> 0.181
#plutao = 4,74 = 1.00 ==> 0.159



'''
Sugestoes:
1- Investigue o efeito de jupiter em marte
2- Explore a orbita de um planeta em um sistema binario de estrelas

'''