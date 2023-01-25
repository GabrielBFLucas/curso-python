"""
Iniciar com letra, pode conter numeros, separar _, letras minusculas
"""
nome = 'Luiz Otávio'  # str
idade = 32  # int
altura = 1.80  # floot
e_maior = idade > 18  # bool
peso = 80  # int
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))