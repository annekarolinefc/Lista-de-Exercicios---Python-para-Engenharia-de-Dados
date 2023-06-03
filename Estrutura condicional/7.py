'''
7 - Uma empresa decide dar aumento de 30% aos funcionários com salários inferiores a R$1000,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso o funcionário não tenha direito ao aumento.
'''

def inserir_aumento(salario):
    if salario<1000:
        salario = salario * 1,3
        return salario 
    else:
        return 'O funcionário não tem direito a um aumento.'