"""
Funções (def) em Python

"""
# ## A FORMA ABAIXO NAO É UMA BOA PRATICA DE PROGRAMAÇÃO ##
# variavel = 'valor' #escopo global
#
# def func():
#     print(variavel)
#
# def func2():
#     variavel = 'Outro valor' #escopo local
#     print(variavel)
#
# func()
# func2()
#
# print(variavel)

##################################################
# ## A FORMA ABAIXO É UMA BOA PRATICA DE PROGRAMAÇÃO ##
#   ## POIS PODE CAUSAR COMPORTAMENTOS ESTRANHOS ##
#
# variavel = 'valor' #escopo global
#
# def func():
#     print(variavel)
#
# def func2():
#     global variavel
#     variavel = 'Outro valor' #escopo local
#     print(variavel)
#
# func()
# func2()
#
# print(variavel) # passou a ser local

##################################################
# ## A FORMA ABAIXO É UMA BOA PRATICA DE PROGRAMAÇÃO ##
#   ##   POIS SETOU A FUNÇAO COMO VARIAVEL GLOBAL  ##
#
# variavel = 'valor' #escopo global
#
# def func():
#     print(variavel)
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c') #trocou o V pelo C
#     return arg
#
# func()
# outra_variavel = func2(arg=variavel)
#
# print(outra_variavel)

##################################################
# ## A FORMA ABAIXO É UMA BOA PRATICA DE PROGRAMAÇÃO ##
#   ##   POIS TRAVALHO A FUNÇAO COMO VARIAVEL LOCAL  ##
#
# def func():
#     outra_variavel = 'Luiz Otávio' # escopo local
#     return outra_variavel
#
# def func2(arg):
#     print(arg)
#
# var = func()
# func2(var)

print(123 + 0.3)