'''
11 - Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.
'''

def dia_do_mes(numero):
    if numero==1:
        return 'Janeiro'
    elif numero == 2:
        return 'Fevereiro'
    elif numero == 3:
        return 'Março'
    elif numero == 4:
        return 'Abril'
    elif numero == 5:
        return 'Maio'
    elif numero == 6:
        return 'Junho'
    elif numero == 7:
        return 'Julho'
    elif numero == 8:
        return 'Agosto'
    elif numero == 9:
        return 'Setembro'
    elif numero == 10:
        return 'Outubro'
    elif numero == 11:
        return 'Novembro'
    elif numero == 12:
        return 'Dezembro'
    else:
        return 'Nao existe mês com esse numero.'
    
num_input = int(input('Insira um numeto entre 1 e 12:'))
result = dia_do_mes(num_input)
print(f'O mês referente a {num_input}: {result}')