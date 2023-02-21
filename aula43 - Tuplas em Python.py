"""
Tuplas em Python

# Na tupla não é possivel adc, alterar, remover itens
# Já na lista é possivel.
"""
# t1 = (1, 2, 3 ,'a', 'Luiz Otávio')
#
# print(t1, type(t1))
# print(t1[4]) #indice 4

##############################
#### PARA ITERAR MINHA LISTA ###
# t1 = (1, 2, 3 ,'a', 'Luiz Otávio')
#
# for v in t1:
#     print(v)

##############################
#### PARA FATIAR MINHA LISTA ###
# t1 = (1, 2, 3 ,'a', 'Luiz Otávio')
#
# print(t1[2:])

##############################
#### PARA CRIAR A TUPLA SEM PARENTESES TBM FUNCIONA ###
# t1 = 1, 2, 3 ,'a', 'Luiz Otávio'
#
# print(t1)

##############################
#### PARA CRIAR A TUPLA COM UM ELEMENTO APENAS ###
# t1 = 1, #basta colocar um vírgula após o índice
#
# print(t1, type(t1))

##############################
#### PARA CONCATENAR UMA TUPLA ###
# t1 = 1,2,3,4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2
#
# print(t3, type(t3))

##############################
#### PARA DESEMPACOTAR UMA TUPLA EM VARIÁVEIS###
# t1 = 1,2,'Luiz',4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2
#
# n1, n2, n3, *_, n10 = t3
# print(n3, type(n3))
# print(n10, type(n10))

##############################
#### PARA REPETIR A TUPLA USANDO O MULTIPLICADOR###
# t1 = (1,2,'Luiz',4,5) * 20
#
# print(t1, type(t1))

##############################
#### PARA CONVERTER TUPLA EM LISTA###
t1 = (1,2,3,4,5)
t1 = list(t1) #converteu tupla em lista
# para converter de lista para tupla é assim:
## t1 = tuple(t1)
t1[3] = 3000 #alterou o índice 3 de (4 para 3000)

print(t1, type(t1))