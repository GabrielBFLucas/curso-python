"""
Operadores Lógicos
And, Or, Not
In e In not

"""

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd ==senha:
    print('Usuário logado no sistema')
else:
    print('Usuario ou senha inválido.')
