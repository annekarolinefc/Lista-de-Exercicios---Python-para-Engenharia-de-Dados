'''
Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado.
'''

def soma(numero):
    soma = 0
    for num in range(0, numero+1): 
        soma = soma + num
    return soma

numero_input = int(input('Insira um numero: ')) 
print(f'Numero informado: {numero_input}')
print(f'Soma de 1 até {numero_input}: {soma(numero_input)}\n')