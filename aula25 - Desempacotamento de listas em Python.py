"""
Desempacotamento de listas em Python
"""
lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista,penultimo_da_lista, ultimo_da_lista = lista
#                             -2                   -1
print(n2, penultimo_da_lista, ultimo_da_lista)

