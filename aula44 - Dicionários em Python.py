"""
Dicionários em Python

# São similares a lista porem eu controlo o indice (chaves)

* == - SE USA UMA REFERÊNCIA
* .copy - SE USA UMA COPIA RAZA
* import copy - SE USA UMA COPIA PROFUNDA

- TUPLAS SÃO IMUTÁVEIS então é necessário converter em lista

"""
import copy

###### GERALMENTE USAM ASSIM PARA CRIAR DICIONÁRIO #######

# d1 = {'chave1':'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave' #para add nova chave
#
# print(d1, type(d1))

#################################################
# d1 = {'chave1':'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave' #para add nova chave
#
# print(d1['chave1'], type(d1)) #para acessar um índice(chave)

#################################################
###### OUTRA FORMA DE CRIAR DICIONÁRIO #######

# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave' #para add nova chave
#
# print(d1['chave1'], type(d1))

#################################################
###### GERALMENTE USAM ASSIM PARA CRIAR DICIONÁRIO #######
#
# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# print(d1[(1,2,3,4)])

#################################################
###### ERROS COMUNS A0 CRIAR DICIONÁRIO #######

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# print(d1[('naoexiste')])

#################################################
###### PARA CONTORNAR O ERRO ACIMA #######
#
# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# d1['naoexiste'] = 'Agora existe.'
# if 'naoexiste' in d1:
#     print(d1[('naoexiste')])

#################################################
###### OUTRA MANEIRA PARA CONTORNAR O ERRO ACIMA #######

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# d1['nomedachave'] = 'Agora existe.'
# if d1.get ('nomedachave') is not None:
#     print(d1.get('nomedachave'))

#################################################
###### OUTRA MANEIRA PARA CONTORNAR O ERRO ACIMA #######
##### PARA ATUALIZAR O VALOR DA CHAVE JÁ EXISTENTE #####

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# d1['str'] = 'Agora existe.' #se comentar essa linha veremos VALOR
# if d1.get ('str') is not None:
#     print(d1.get('str'))

#################################################
###### OUTRA MANEIRA PARA CONTORNAR O ERRO ACIMA #######
##### PARA ATUALIZAR O VALOR DA CHAVE JÁ EXISTENTE #####

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# d1.update({'nova_chave' : 'novo_valor'})
#
# if d1.get ('nova_chave') is not None:
#     print(d1.get('nova_chave'))

#################################################
###### OUTRA MANEIRA PARA CONTORNAR O ERRO ACIMA #######
##### PARA EXCLUIR ALGUM VALOR DA CHAVE JÁ EXISTENTE #####

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# del d1['str']
# print(d1)

#################################################
##### PARA CHECAR ALGUM VALOR DA CHAVE JÁ EXISTENTE #####

# d1 = {
#     'str' : 'valor',
#     123 : 'Outro Valor',
#     (1,2,3,4) : 'Tupla',
# }
#
# print('str' in d1) # True (Existe dentro da chaves)
# print('str' in d1.keys()) # True (Tbm existe / outra forma de encontrar valores)
# print('valor' in d1.values()) # True (Tbm existe dentro de d1)
# print(len(d1)) # Tamanho (3 pares de chaves/valores dentro de d1)

#################################################
##### PARA ITERAR ALGUM VALOR DE CHAVES #####

# d1 ={
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'Tupla',
# }
#
# # for v in d1.values(): #veremos apenas os valores
# # for v in d1:  # veremos apenas as chaves
# # for v in d1.items(): #veremos tudo
# for v in d1.items(): #acessaremos chave e valor separadamente
#     print(v[0], v[1])

#################################################
##### PARA DESEMPACOTAR ALGUM VALOR DE CHAVES #####

# d1 ={
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'Tupla',
# }
#
# for k, v in d1.items(): #acessaremos chave e valor separadamente
#     print(k, v)

#################################################
##### CRIAR DICIONARIO DENTRO DE DICIONARIO  / ITERANDO #####

# clientes = {
#     'cliente1' : {
#         'nome' : 'Luiz',
#         'sobrenome' : 'Otávio',
#     },
#     'cliente2' : {
#         'nome' : 'João',
#         'sobrenome' : 'Moreira',
#     },
# }
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

#################################################
###### METODO ERRADO DE FAZER COPIA RAZA DE DICIONARIO #####

# d1 = {1: 'a', 2:'b', 3:'c'}
# v = d1 # OS ITENS SÃO EXATAMENTE IGUAIS
#
# v[1] = 'Luiz' # DESEJO ALTERAR ITEM 1 EM V
#
# print(v == d1)
# print(d1)
# print(v)

#################################################
###### METODO CORRETO DE FAZER COPIA RAZA DE DICIONARIO #####

# d1 = {1: 'a', 2:'b', 3:'c'}
# v = d1.copy() # OS ITENS SÃO EXATAMENTE IGUAIS
#
# v[1] = 'Luiz' # DESEJO ALTERAR ITEM 1 EM V
#
# print(v == d1)
# print(d1)
# print(v) # AGORA APENAS O ITEM 1 DE V FOR ALTERADO

#################################################
###### METODO CORRETO DE FAZER COPIA RAZA DE DICIONARIO #####

# d1 = {1: 'a', 2:'b', 3:'c', 'd': ['Luiz', 'Otávio']}
# v = d1.copy() # OS ITENS SÃO EXATAMENTE IGUAIS
#
# v[1] = 'Luiz' # DESEJO ALTERAR ITEM 1 EM V
#
# print(v['d'] [0]) # ACESSAMOS APENAS O ITEM 0 de d

#################################################
###### METODO INCORRETO DE FAZER COPIA RAZA ALTERANDO DADOS DE DICIONARIO #####

# d1 = {1: 'a', 2:'b', 3:'c', 'd': ['Luiz', 'Otávio']}
# v = d1.copy() # OS ITENS SÃO EXATAMENTE IGUAIS
#
# v[1] = 'Luiz' # DESEJO ALTERAR ITEM 1 EM V
# v['d'] [0] = 'Joãozinho' # DESEJO ALTERAR ITEM 0 EM D EM V
#
# print(d1)
# print(v)

#################################################
###### METODO CORRETO USANDO BIBLIOTECA COPY PARA FAZER COPIA RAZA ALTERANDO DADOS DE DICIONARIO #####

# import copy
#
# d1 = {1: 'a', 2:'b', 3:'c', 'd': ['Luiz', 'Otávio']}
# v = copy.deepcopy(d1) #copia profunda
#
# v[1] = 'Luiz' # DESEJO ALTERAR ITEM 1 EM V
# v['d'] [0] = 'Joãozinho' # DESEJO ALTERAR ITEM 0 EM D EM V
#
# print(d1)
# print(v)

#################################################
###### METODO DE TRANSFORMAR LISTA EM DICIONARIO #####

# lista = [
#     ['c1', 1], #similar a chave e valor
#     ['c2', 2],
#     ['c3', 3],
# ]
#
# d1 = dict(lista)
# print(d1)

#################################################
###### METODO DE TRANSFORMAR LISTA EM DICIONARIO #####

# lista = [
#     ('c1', 1), # tuplas
#     ('c2', 2),
#     ('c3', 3),
# ]
#
# d1 = dict(lista)
# print(d1)
# print(d1['c3'])

#################################################
###### METODO DE ELIMINAR ITEM DA LISTA DO DICIONARIO #####

# d1 = {
#     1: 2,
#     2: 3,
#     4: 5,
# }
#
# d1.pop(1) #vai elimirar o item especificado da lista
# # d1.popitem() #vai elimirar o último item da lista
# print(d1)

#################################################
###### METODO DE CONCATENAR ITENS DA LISTA DO DICIONARIO #####
### OPERADOR DE + NAO IRÁ FUNCIONAR NESTE CASO, ENTÃO... ####

d1 = {
    1: 2,
    2: 3,
    4: 5,
}
d2 = {
    'a': 'b',
    'c': 'd',
}

d1.update(d2) # somando/concatenando os dois dicionarios
print(d1)