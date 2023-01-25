""""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

booleano = True
inteiros = 10
flutuante = -10.10
strings = 'Textos'
"""
# Para acessar lista ao contrario ou
# substituir itens da lista

# #         0   1    2    3    4
# lista = ['A','B', 'C', 'D', 10.5]
# #        -5  -4   -3   -2   -1
# lista[4] = 'Qualquer outra coisa.'
#
# print(lista[::-1])

# """"""""""""""""""""""""""""""""""""""
# # Para inserir, adicionar, deletar índices da lista
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [1,2,3,4,5,6,7,8,9]
# l4 = [1,2,3,4,5,6,7,8,9]
# l5 = list(range(1,50, 8)) # criou uma lista 1 a 50 multiplos de 8
#
# l1.extend(l2) # extendeu a l2 na l1
# l2.append('b') # ultimo indice passou a ser b
# l2.insert(0, 'banana') # indice 0 passou a ser banana
# l2.pop(2) # removeu indice 2 (numero 5)
# del(l3[::2]) # deletou de 1 em 1
#
# print(l1)
# print(l2)
# print(l3)
# print(max(l4)) # pegou o maior valor da lista l4
# print(min(l4)) # pegou o menor valor da lista l4
# print(l5)

# """""""""""""""""""""""""""""""""""""
##############JOGO PALAVRA SECRETA##############

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break


    letra = input('Digite uma letra em minusculo: ')

    if len(letra) > 1:
       print('Ahhh isso não vale, digite apenas uma letra.')
       continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Afffzzz: a letra "{letra}" NÃO existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCEÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()





