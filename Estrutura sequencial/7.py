'''
Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado. 
'''

a = int(input('Insira um valor inteiro:'))
antecessor = a - 1
sucessor = a + 1 
dobro = a*2
metade = a/2

print(f'Antecessor: {antecessor}')
print(f'Sucessor: {sucessor}')
print(f'Dobro: {dobro}')
print(f'Metade: {metade}')