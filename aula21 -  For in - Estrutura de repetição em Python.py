"""
For in em Python
Interando strings com for
Função range(start=0, stop, step=1)
"""
# texto ='Python'
#
# for n, letra in enumerate(texto):
#     print(n, letra)

''''''''''''''''''''''''''''''''''''
#           (start, step, stop)
# for n in range(20, 10, -1):
#     print(n)
''''''''''''''''''''''''''''''''''''
# texto = 'Python'
# nova_string = ''
#
# for letra in texto:
#     if letra == 't':
#         nova_string = nova_string + letra.upper()
#     elif letra == 'h':
#         nova_string +=letra.upper()
#     else:
#         nova_string += letra
# print(nova_string)
''''''''''''''''''''''''''''''''''''
texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        continue #break (Py) / #continue (PyHon) - Upper TH
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string +=letra.upper()
    else:
        nova_string += letra
print(nova_string)
