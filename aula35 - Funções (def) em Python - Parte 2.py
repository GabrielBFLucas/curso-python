"""
Funções (def) em Python - Parte 2 - return
"""
# def funcao(var):
#     print(var)
#
# funcao('Valor que eu quero')

# ##########################################
# def funcao(var):
#     return var
#     print('Isso nao será executado.')
#
# variavel = funcao('Valor que eu quero.')
#
# if variavel:
#     print(variavel)
# else:
#     print('Nenhum valor.')

##########################################
# def divisao(n1, n2):
#     if n2 > 0:
#      return n1 / n2
#
# divide = divisao(8, 0)  #Nao é permitido divisao por Zero
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida')

##########################################
# def divisao(n1, n2):
#     if n2 == 0:
#       return
#
#     return n1 / n2
#
# divide = divisao(8, 4)  #Nao é permitido divisao por Zero
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida')

##########################################
# def dumb():
#     return 1.1 #RETORNANDO FLOAT
#
# var = dumb()
# print(var, type(var))

##########################################
# def dumb():
#     return [1,2,3,4,5,6,7,8,9] #RETORNANDO LISTA
#
# var = dumb()
# print(var, type(var))

# ##########################################
# def f(var):
#  print(var)
#
# def dumb():
#  return f
#
# var = dumb()('E colocar o meu valor aqui.')

##########################################
def dumb():
    return ('Luiz' , 'Otávio')

var = dumb()

print(var[0], type(var))
