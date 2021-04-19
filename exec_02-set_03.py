"""
Exercicios aula 02 - 09
x[n+1] = x[n] + (dx/dt)*h
  x' = -(7/9)x -(8/9)y
y[n+1]  = y[n] + (dy/dt)*h
  y' = -(4/9)x +(7/9)y
"""

import matplotlib.pyplot as plt

def solve(N, x0, y0):
 #Definindo as cond inicias
    a = 0.0         #t inicial
    b= 200.0        #t final
    h = (b-a)/N     #valor do paaso  
    x = [x0]    
    y = [y0]    
    t = [a]
    CI = "x0 = %0.1f, y0 = %0.1f" %(x0, y0)

    for n in range(N):
        x.append(x[n] + (-(7/9)*x[n] - (8/9)*y[n])*h)
        y.append(y[n] + ((1/5)* y[n] - (9/5)*y[n])*h)   
        t.append(t[n]+h)
        
    return t, x, y, CI

t1, x1, y1, CI1 = solve(1000, 3.0, 1.5 )
t2, x2, y2, CI2 = solve(1000, 2.0, -1.0 )
t3, x3, y3, CI3 = solve(1000, 1.5, -3.0 )

plt.grid(True) 
plt.figure(1)  
plt.plot(x1, y1, label=CI1)
plt.plot(x2, y2, label=CI2)
plt.plot(x3, y3, label=CI3)
plt.legend(loc=1)
  
'''Gráficos de x por t e y por t utilizando subplot;'''

plt.figure(2)
plt.subplot(211)
plt.plot(t1, x1)
plt.grid(True)
plt.subplot(212)
plt.plot(t1, y1)
plt.grid(True) 