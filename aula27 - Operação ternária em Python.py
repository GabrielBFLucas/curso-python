"""
Operador ternário em Python
"""
# logged_user = False
#
# if logged_user:
#     msg = "Usuário Logado."
# else:
#     msg = "Usuário precisa logar."
#
# print(msg)

#######################################
####  Mesma coisa do codigo acima  ####

# logged_user = True
# msg = "Usuário Logado." if logged_user else "Usuario precisa logar."
#
# print(msg)

#######################################

# idade = 17
#
# if idade>=18:
#     print('Pode acessar.')
# else:
#     print("Não pode acessar")

#######################################
####  Mesma coisa do codigo acima com Input ####

idade = input('Digite sua idade: ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade>=18)

    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg)