# 1 receber um num e exibir o maior
'''
numero1 = 100
numero2 = 50

if numero1 > numero2:
    print("numero 1 maior que o 2")
else:
    print("numero 2 é maior que o 1")
'''

# 2 receber um numero e exibir a raiz caso o numero seja positivo
'''numero = int(input("digite um numero:\n"))
raiz = float(numero)**0.5
if numero >= 0:
    print("A raiz de :", numero, '\n' "é :", raiz)
else:
    print("numero invalido!")
'''
# 3 imprima a raiz do numero se positivo se não o quadrado
'''
numero = int(input("insira um numero!"))
if numero >= 0:
    print(float(numero)**0.5)
else:
    print(float(numero)**2)
'''
# 4 Calculo do IMC
peso = float(input("insira seu peso !"'\n'))
altura = float(input("insira sua altura!"'\n'))
imc = peso/(altura**2)
if imc < 18.5:
    print(imc, "Você esta abaixo do peso")
elif imc >= 18.6 or 24.9:
    print(imc, "Saudavel")
elif imc >= 25.0 or 29.9:
    print(imc, "Ta Gordola")
elif imc >= 30.0 or 34.9:
    print(imc, "Obeso grau 1")
elif imc >= 35.0 or 39.9:
    print(imc, "Obeso grau 2(severa)")
elif imc >= 40:
    print(imc, "Obeso  grau 3 (morbida)")
else:
    print("sai daqui ta trollando cara ?")
