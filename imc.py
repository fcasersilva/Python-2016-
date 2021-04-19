# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"Calculando o imc"

peso = float(raw_input('Insira o peso em kg\n'))
altura = float(raw_input('Insira a altura em m\n'))

imc = (peso)/(altura**2)

if imc < 17.00:
    print "Seu IMC eh %0.2f:" %(imc), "Muito abaixo do peso"

elif imc >= 17.00 and imc <= 18.49:
    print "Seu IMC eh %0.2f:" %(imc), "Abaixo do peso"
    
elif imc >= 18.50 and imc <= 24.99:
    print "Seu IMC eh %0.2f:" %(imc), "Peso normal. Fica traqnuilo mô quiridu!"
    
elif imc >= 25.00 and imc <= 29.99:
    print "Seu IMC eh %0.2f:" %(imc), "Acima do peso"

elif imc >= 35.00 and imc <= 39.99:
    print "Seu IMC eh %0.2f:" %(imc), "Obesidade II (severa)"

elif imc >= 40.00:
    print "Seu IMC eh %0.2f:" %(imc), "Obesidade III (morbida)"
    
while True:
    massa  = float(raw_input('Insira a massa. Digite 0 para encerrar.\n'))
    altura = float(raw_input('Insira a altura. Digite 0 para encerrar.\n'))
    
    if massa == 0 or altura == 0:
        print 'Progama encerrado!'
        break
    
    
    