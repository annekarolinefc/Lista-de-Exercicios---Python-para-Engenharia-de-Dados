""" 
1.	Crie uma lista contendo 10 valores inteiros aleatórios, entre 1 e 20. Imprima:
a.	O maior valor, o menor valor, a soma e a média dos valores na lista
b.	Ordene a lista, e em seguida, a imprima em ordem crescente
c.	Imprima a lista em ordem decrescente
d.	Solicite ao usuário que informe um valor e imprima a quantidade de ocorrências do valor na lista. Imprima uma mensagem, caso o valor não se encontre na lista

"""
from random import sample
lista_aleatoria = sample(range(1,101), 10)
print (f'Lista: {lista_aleatoria}\n')
print(f'Exercicio a:')
print (f'Maior valor: {max(lista_aleatoria)}')
print (f'Menor valor: {min(lista_aleatoria)}')
print (f'Soma: {sum(lista_aleatoria)}')
print (f'Media: {sum(lista_aleatoria)/(len(lista_aleatoria))}')

print(f'\nExercicio b:')
lista_aleatoria.sort()
print(f'Lista em ordem crescente: {lista_aleatoria}')

print(f'\nExercicio c:')
print(f'Lista em ordem decrescente: {lista_aleatoria[::-1]}')

print(f'\nExercicio d:')
numero = int(input('Insira um numero: '))
""" 
ocorrencia = 0
for elemento in lista_aleatoria:
    if elemento == numero:
        ocorrencia = ocorrencia + 1
"""
if numero in lista_aleatoria:
    print(f'Numero de ocorrencias: {lista_aleatoria.count(numero)}\n')
else:
    print(f'Numero de ocorrencias: {lista_aleatoria.count(numero)}\n')