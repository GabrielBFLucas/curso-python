"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""
# usuario = input('Digite um usuario: ')
# def saudacao(msg = 'Olá', nome = usuario):
#     print(msg,nome)
#
# saudacao()
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.
"""
# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))
# def somando(n1, n2, n3):
#     return n1 + n2 + n3
#
# soma = somando(n1, n2, n3)
# print(f'O total da soma é {soma}')

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
# n1 = int(input('Digite um numero: '))
# n2 = 0.10 * n1
# def somando(n1, n2):
#     return n1 + n2
#
# soma = somando(n1, n2)
# print(soma)

"""
4 - Fizz Buzz - Se o parâmentro da função for divisível por 3, retorne fizz,
se o parâmentro da função for divisível por 5, retorne buzz. Se o parâmentro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o 
número enviado.
"""
numero = int(input('Digite um numero: '))
def fb(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero
print(fb(numero))
