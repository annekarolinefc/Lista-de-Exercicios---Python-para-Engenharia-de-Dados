'''
Faça um programa que leia um número e que calcule o fatorial deste número.
'''

fat = int(input('Insira um numero: '))
if fat < 0:
    print('O fatorial nao pode ser calculado.')
else :
    fatorial = 1 
    for i in range(1, fat + 1):
        fatorial = fatorial * i
print(f'Fatorial de {fat}: {fatorial}\n')