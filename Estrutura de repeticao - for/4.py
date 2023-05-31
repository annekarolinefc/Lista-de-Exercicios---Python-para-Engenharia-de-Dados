'''
Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados.
'''


def imprime_inteiros(num1, num2):
    list = []
    if num1>num2:
        for i in range(num2+1, num1):
            list.append(i)
    elif num1<num2:
        for i in range(num1+1, num2):
            list.append(i)
    return list

num_1=int(input("Digite o primeiro número inteiro: "))
num_2=int(input("Digite o segundo número inteiro: "))   
l = imprime_inteiros(num_1, num_2)
#l = imprime_inteiros(num1, num2)
print(l)