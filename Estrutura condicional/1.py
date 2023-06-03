'''
    1- Faça um programa que receba dois números e mostre o maior e o menor. 
    Emita uma mensagem, caso os dois sejam iguais.
'''

def testaNumero(num1, num2):
    if num1>num2:
        print(f'{num1} é maior que {num2}.')
    elif num2>num1:
        print(f'{num2} é maior que {num1}.')
    else:
        print(f'Os numeros são iguais: {num1} e {num2}')

num1 = input('Insira o primeiro numero:')
num2 = input('Insira o segundo numero:')    
testaNumero(num1, num2)