"""
Funções ()def) em Python - *args **kwargs

"""
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# n1, n2, *n = lista # Desempacotando os dois primeiros valores
# print(n1, n2, n) # Empacotando o restante da lista numa variavel *n

##############################################
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# print(*lista, sep='-') # Quando se usa o * ta desempacotando sem a [] ou ()

##############################################
# def func(*args):
#     args = list(args) # uma tulpla para uma list
#     args[0] = 20 # O primeiro indice mudou de 1 para 20
#     print(args)
#
# func(1,2,3,4,5)

##############################################
# def func(*args):
#   for v in args:
#       print(v) # a cada volta um indice da lista
#
# func(1,2,3,4,5)

##############################################
# def func(*args):
#     print(args[0]) #apenas o primeiro indice da lista
#
# lista = [1,2,3,4,5]
# func(*lista) #Desempacotou

##############################################
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2) #Desempacotou

##############################################
# def func(*args, **kwargs): #Por convenção se usa *args/**kwargs mas não é obrigatorio
#     print(args) # cada indice dentro da tupla
#     print(kwargs) # argumentos com palavra dentro de chaves {}
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

##############################################
def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)