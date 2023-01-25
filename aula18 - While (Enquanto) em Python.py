"""
While em Python
utilizando para realizar ações enquanto
uma condição for verdadeira.

Rquisitos: Entender condições e operadores
"""
# x = 0
# while x<100:
#     print(x)
#     x = x + 1
# print('Acabou!')

while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operator = input('Digite um operador: ')
    sair = input('Deseja SAIR? s[im] ou n[ão]: ')

    if sair == 's':
        break


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - * /
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)

