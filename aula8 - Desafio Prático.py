"""
*criar variaveis para nome(str), idade (int)
*criar altura (flooat) e peso (flooat) de uma pessoa
*obter o ano de nascimento de uma pessoa (baseado na idade e ano atual)
*obter IMC da pessoa com 2 casas decimais
*exibir um texto com todos os valores na tela usando o F-String (com as chaves)
"""

nome = 'Luiz Otávio'
idade = 32
altura = 1.8
peso = 80.5
nascimento = 2022 - idade
imc = peso / altura ** 2

print('{n} nasceu em {nas}, tem {i} anos, {a} de comprimento, {kg} quilos, possui um imc de {im:.2f}' .format(n=nome, nas=nascimento, i=idade, a=altura, kg=peso, im= imc))

print(f'{nome} nasceu em {nascimento}, tem {idade} anos, {altura} de comprimento, {peso} quilos, possui um imc de {imc:.2f}')


