"""
Expressões lambda (funções anônimas) em Python
"""
# def funcao(arg, arg2):
#     return arg * arg2
#
# var = funcao(2,2)
# print(var)

#################################################
############ MESMA CONTA DA FUNÇÃO ACIMA ############
# a = lambda x,y: x * y
# print(a(2,2))

#################################################

# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 7],
#     ['P4', 50],
#     ['P5', 8],
# ]
#
# def func(item):
#     return item[1]
# lista.sort(key=func, reverse=True) #Reverte a lista do mais caro para o mais barato
# print(lista)

#################################################
############ MESMA ORDENAÇÃO DA FUNÇÃO ACIMA ############

# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 7],
#     ['P4', 50],
#     ['P5', 8],
# ]
#
# lista.sort(key=lambda item: item[1], reverse=True) #Reverte a lista do mais caro para o mais barato
# print(lista)

#################################################
############ MESMA ORDENAÇÃO DA FUNÇÃO ACIMA ############

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda item: item[1], reverse=True)) #Reverte a lista do mais caro para o mais barato
