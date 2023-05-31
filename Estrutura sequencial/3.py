'''
3.	Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação).
'''
import math 

coef_a = float(input('Insira o coeficiente a: '))
coef_b = float(input('Insira o coeficiente b: '))
coef_c = float(input('Insira o coeficiente c: '))
delta = coef_b**2 - 4*coef_a*coef_c
if delta >=0:
    x1 = (-coef_b+math.sqrt(delta))/(2*coef_a)
    x2 = (-coef_b-math.sqrt(delta))/(2*coef_a)
print(f'Raízes da equação de segundo grau: {x1} e {x2}')