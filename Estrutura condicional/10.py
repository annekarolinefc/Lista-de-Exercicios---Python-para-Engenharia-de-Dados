'''
10 - Faça um programa que leia o um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número.
'''

def dia_da_semana(numero):
    if numero==1:
        return 'Segunda'
    elif numero == 2:
        return 'Terça'
    elif numero == 3:
        return 'Quarta'
    elif numero == 4:
        return 'Quinta'
    elif numero == 5:
        return 'Sexta'
    elif numero == 6:
        return 'Sábado'
    elif numero == 7:
        return 'Domingo'
    else:
        return 'Nao existe dia da semana com esse numero.'
    
num_input = int(input('Insira um numero entre 1 e 7: '))
result = dia_da_semana(num_input)
print(f'O dia da semana referente a {num_input}: {result}')