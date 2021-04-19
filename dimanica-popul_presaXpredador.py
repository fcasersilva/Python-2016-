"""
DINAMICA POPULACIONAL
(Modelo de Lotka-Volterra)

C = população de coelhos
L = população de lobos

dC/dt = k*C - a*L*C
dL/dt = -r*L + b*C*L

k = 0.08 (taxa de crexcimento natural de coelhos)
a = 0.001 (taxa de diminuição natural de coelhos)
r = 0.02 (taxa de descrecimento natural de lobos (nao tem predadores))
b = 0.00002 (fator de aumento da taxa de cresc natural de lobos)

condiçoes de equilibio:
Lobos = 80
Coelhos = 1000
"""
import matplotlib.pyplot as plt

def lokta (k, a, r, b, C0, L0, t0, h, N):
    C = [C0]
    L = [L0]
    t = [t0]
    
    for n in range(N):
        C.append(C[n] + ( k*C[n] -a*C[n]*L[n])*h)
        L.append(L[n] + (-r*L[n] + b*C[n+1]*L[n])*h)
        t.append(t[n] + h)
        if C[n] < 1.0 or L[n] < 1.0:
            break
    
    plt.close('all') #fechar todos os possiveis graficos abertos
    plt.plot (t, L, 'r')
    plt.plot (t, C, 'b')
    plt.grid(True)

## Grafico do espaço de fase
#    plt.plot(L,C)
#    plt.ylabel('Pop. de Coelhos')
#    plt.xlabel('Pop. Lobos')
#    
#lokta  (k,    a,     r,    b,       C0,     L0,   to,  h,   N)
lokta   (0.08, 0.001, 0.02, 0.00002, 1000.0, 90.0, 0.0, 0.1, 50000  )