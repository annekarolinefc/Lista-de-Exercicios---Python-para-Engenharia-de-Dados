'''
Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos.
'''
qtd_pessoas = 10
soma_pesos = 0

for i in range(qtd_pessoas):
    peso = float(input('Digite o peso da pessoa: '))
    soma_pesos = soma_pesos + peso

media_pesos = soma_pesos / qtd_pessoas

print(f'A media dos pesos e {round(media_pesos, 2)}')