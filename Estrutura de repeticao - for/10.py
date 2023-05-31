'''
Faça um programa que leia um número e que imprima na tela se o número é primo ou não.
'''

numero = int(input('Insira um numero inteiro: ')) 
if numero>1:
    for i in range(2, int(numero/2)+1):
        if numero%i == 0:
            print(f'{numero} nao e um número primo.')
            break
    else:
        print(f'{numero} e um numero primo')
else:
    print(f'{numero} nao e um numero primo.')