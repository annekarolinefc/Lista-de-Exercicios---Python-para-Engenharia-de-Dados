""" 
2.	Crie duas listas com 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma que contenha a soma dos elementos de mesma posição das duas listas originais, e outra que contenha a multiplicação dos valores de mesma posição. Imprima em seguida as 3 listas.
"""

from random import sample
l1 = sample(range(1,50), 10)
l2 = sample(range(1,50), 10)
l3 = [x + y for x, y in zip(l1, l2)]
l4 = [x * y for x, y in zip(l1, l2)]


print("Lista 1:", l1)
print("Lista 2:", l2)
print("Soma:", l3)
print("Multiplicacao:", l4)