"""
1 - Crie uma funçao1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.

"""
# func = input('Digite algo: ') #escopo global
#
# def ola_mundo():
#     return func
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)

"""
2 -  Crie uma funçao1 que recebe uma função2 como parâmetro e retorne o valor da 
função2 executada. Faca a função1 executar duas funçoes que recebem um numero
diferente de argumentos.
"""
nome = input('Digite um nome: ') #escopo global

def fala_oi():
    print(f'Oi {nome}')

def saudacao():
    global nome
    nome = 'Luiz Otávio' #escopo local
    saudacao = 'Olá'
    print(f'{saudacao} {nome}')

fala_oi()
saudacao()
