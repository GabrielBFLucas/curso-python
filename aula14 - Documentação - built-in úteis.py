"""
Existem varias formas de contornar quebras feitas pelo usuário,
basta consultar a documentação.

"""
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')

