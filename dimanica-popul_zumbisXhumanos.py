"""
DINAMICA POPULACIONAL
(Modelo de Lotka-Volterra)

H = população de humanos
Z = população de zumbis
alfa = tx infeção
beta = tx erradicação
tau = tx cresc aprendizado zumbi
gama = tx cresc aprendizado humano 
M = aprendizado max zumbi
N = aprendizado max humano
b = tx natalidade humana
d = tx obito humana
K = pop max mundial suportavel
t0 = tempo inicial
H0 = pop humana inicial
Z0 = pop zumbi inicial
h = passo
IT = iteraçoes
"""
import matplotlib.pyplot as plt

def apocalipse (alfa0, beta0, tau, gama, M, N, b, d, K, t0, H0,Z0, h, IT):
    r = b-d
    t = [t0] #meses
    H = [H0]
    Z = [Z0]
    alfa = [alfa0]
    beta = [beta0]
    
    for n in range(IT):
        # Varição da População humana:
        H.append(H[n] + (r*H[n] -(r/K)*H[n]**2 - alfa[n])*H[n]*Z[n]*h)
        
        #Varição da População Zumbi:
        Z.append(Z[n] + (alfa[n]*H[n]*Z[n]     - beta[n]*H[n+1]*Z[n] + 1.0*(d*H[n] + (r/K)*H[n+1]**2))*h)

        #curva de aprendizado Zumbi:
        alfa.append(alfa[n] + tau*(M - alfa[n])*h)        

        #Curva de prendizado Humano
        beta.append(beta[n] + gama*(N-beta[n])*h)        
                
        t.append(t[n] + h)
        
        if H[n] < 1.0E-9 or Z[n] < 1.0E-9:
            break
    
    plt.close('all') #fechar todos os possiveis graficos abertos
    plt.plot (t, H, 'b')
    plt.plot (t, Z, 'r')
    plt.grid(True)
    
#    #Grafico do espaço de fase
#    plt.plot(Z,H)    
#    plt.ylabel ('Pop Humanos')
#    plt.xlabel ('Pop Zumbi')

    print 'População Humana Final = %s' %(H[-1])
    print 'População Zumbi Final = %s' %(Z[-1])

#apocalipse (alfa0, beta0, tau,  gama, M,   N,     b,     d,       K,    t0,  H0,   Z0,      h,   IT)
apocalipse  (0.3,   0.3,   0.02, 0.1, 0.4, 0.6, 0.0187, 0.00789, 10.0, 0.0, 7.174, 1.0E-9, 0.01, 500000)