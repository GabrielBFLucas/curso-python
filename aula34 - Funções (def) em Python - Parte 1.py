"""
Funções (def) em Python - Parte 1
"""
# def funcao(msg):
#     print(msg)
#
# funcao('Eu posso escrever o que eu quiser aqui.')

###################################################
# def saudacao(msg, nome):
#     print(msg,nome)
#
# saudacao('Olá', 'Luiz Otávio')
# saudacao('Oi', 'Luiz')
# saudacao('Hello', 'Maria')
# saudacao('Olá', 'Otávio')
# saudacao('Olá', 'João')

###################################################
# def saudacao(msg = 'Olá', nome = 'usuário'):
#     print(msg,nome)
#
# saudacao()
# saudacao()
# saudacao('Hello', 'Maria')
# saudacao('Olá', 'Otávio')
# saudacao('Olá', 'João')

###################################################
# def saudacao(msg = 'Olá', nome = 'usuário'):
#     print(msg,nome)
#
# saudacao(nome = 'Zezinho', msg = 'Hi')
# saudacao(nome = 'Pedrinho')
# saudacao()
# saudacao('Hello', 'Otávio')
# saudacao('Oi', 'João')

# ###################################################
# def saudacao(msg = 'Ola', nome = 'usuário'):
#     nome = nome.replace('a', '4')
#     msg = msg.replace('a', '4')
#     print(msg,nome)
#
# saudacao(nome = 'Zezinho', msg = 'Hi')
# saudacao(nome = 'Pedrinho')
# saudacao()
# saudacao('Hello', 'Otavio')
# saudacao('Oi', 'Joao')

###################################################
def saudacao(msg = 'Olá', nome = 'usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '4')
    print(msg,nome)

saudacao(nome = 'Zezinho', msg = 'Hi')
saudacao(nome = 'Pedrinho')
saudacao()
saudacao('Hello', 'Otavio')
saudacao('Oi', 'Joao')