'''
2.	Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
a.	A idade da pessoa no ano atual
b.	A idade que a pessoa terá em 2050
'''

ano_nascimento = int(input('Digite o ano de seu nascimento: '))
ano_atual = 2023
ano_2050 = 2050

print(f'a) Idade da pessoa no ano atual ({ano_atual}): {ano_atual-ano_nascimento}')
print(f'a) Idade da pessoa no ano de 2050: {ano_2050-ano_nascimento}\n')