""" 
4.	Crie uma lista contendo 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma para armazenar os valores pares da primeira lista, e outra para armazenar os valores ímpares. Imprima em seguida as 3 listas.
"""
import random
l1 = [random.randrange(1,40) for x in range(10)]
lpares = [l for l in l1 if (l%2==0)]
limpares = [l for l in l1 if (l%2!=0)]

print(f'Lista com 10 valores aleatorios: {l1}\n')
print(f'Lista de valores pares:{lpares}')
print(f'Lista de valores impares:{limpares}\n')

# -----------Feito na aula-----------
# l1 = [random.randrange(1,40) for x in range(10)]
# lista_pares = []
# lista_impares = []
# for l in l1:
#     if l%2==0:
#         lista_pares.append(l)
#     else:
#         lista_impares.append(l)
        
# print(f'Lista de valores pares:{lista_pares}')
# print(f'Lista de valores impares:{lista_impares}')