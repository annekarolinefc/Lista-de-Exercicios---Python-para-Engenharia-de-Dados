'''
6.	Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom. Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta.
'''
valor_gasto = float(input('Insira o valor gasto pelo cliente (R$): '))
gorjeta = round((0.10 * valor_gasto), 2)
print(f'A gorjeta de R${valor_gasto} => R${gorjeta}\n')