'''
5.	Receba um número positivo, calcule e mostre:
a.	O número digitado ao quadrado
b.	O número digitado ao cubo
c.	A raiz quadrada do número digitado
d.	A raiz cúbica do número digitado.
'''

a = float(input('Insira um numero positivo: '))
quadrado = a**2
cubo = a**3 
raiz_quadrada = a**(1/2)
raiz_cubica = a**(1/3)

print(f'a.	O número digitado ao quadrado: {quadrado}')
print(f'b.	O número digitado ao cubo: {cubo}')
print(f'c.	A raiz quadrada do número digitado: {raiz_quadrada}')
print(f'd.	A raiz cúbica do número digitado: {raiz_cubica}')