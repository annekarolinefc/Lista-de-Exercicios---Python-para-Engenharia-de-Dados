""" 
3.	Considere a seguinte lista: [10, 20, 30, 30, 30, 40, 10, 20]
	Faça um programa que exclua todas as ocorrências do número 30 da lista

"""

list = [10, 20, 30, 30, 30, 40, 10, 20]
# for elemento in list:
#     if elemento == 30:
#         list.remove(elemento)
# print(list)

# Usando list comprehension
lista_sem_30 = [x for x in list if x!=30]
print(lista_sem_30)