""" 
6.	Faça um programa que gere uma lista contendo 6 números aleatórios, de 1 a 60, que serão jogados na Mega-Sena. Em seguida, solicite ao usuário os 6 números sorteados. Imprima a lista contendo os números jogados, e a quantidade de números acertados no sorteio.
"""
"""
import random
lista_aleatoria = [random.randint(1, 60) for x in range(6)]
"""
# criando a lista com os numeros da mega-sena sorteados
from random import sample
lista_aleatoria = sample(range(1,61), 6)

numeros_mega = 6
lista_numeros = []
while numeros_mega!=0:
    num = int(input('Insira um numero: '))
    lista_numeros.append(num)
    numeros_mega = numeros_mega - 1
    
print(f'Números jogados: {lista_numeros}')
print(f'Números da Mega-Sena: {lista_aleatoria}')

acertos = []
for numero in lista_aleatoria:
    if numero in lista_numeros:
        acertos.append(numero)
print(f'Você acertou {len(acertos)} numeros.\n')
#print(f'Quantidade de números acertados: {}')
    