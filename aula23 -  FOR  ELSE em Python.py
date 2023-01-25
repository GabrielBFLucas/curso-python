"""
For / Else em Python
"""
##########VERIFICA INICIO DA PALAVRA##########

# variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']
#
# for valor in variavel:
#     if valor.startswith('J'):
#         print('Começa com J', valor)
#     else:
#         print('Não começa com J', valor)
#

##################################################
# variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']
#
# for valor in variavel:
#     if valor.lower().startswith('j'):
#         comeca_com_j = True
#
# if comeca_com_j:
#     print('Existe uma palavra que começa com J.')
# else:
#     print('Nao existe uma palavra que começa com J.')

##################################################
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
       continue
    print(valor)
