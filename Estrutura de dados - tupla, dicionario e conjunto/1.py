""" 
    1. Crie uma tupla contendo 10 valores determinados por você. Solicite em seguida que o usuário informe um valor. Informe quantas vezes o valor se encontra na tupla. Caso não se encontre, emita uma mensagem informando.
"""

tupla = (1,2,3,4,5,6,7,8,9,10)
valor = int(input('Insira um valor: '))
if valor in tupla:
    print(f'{valor} aparece na tupla {tupla} por {0} vezes.')
else:
    print(f'O valor {valor} não se encontra na tupla {tupla}')