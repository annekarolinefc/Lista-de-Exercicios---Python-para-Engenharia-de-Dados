"""
    Faça um programa que leia um número 
    e que imprima os números ímpares de 
    1 até o número informado. 
"""

x = int(input('Digite um numero: '))
impares = []
for y in range(0, x):
    if (y%2)!=0:
        impares.append(y)
        print(f'{y} => impar')

print(f'\nTodos os impares: {impares}\n')