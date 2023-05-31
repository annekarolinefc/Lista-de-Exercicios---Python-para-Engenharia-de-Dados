'''
Faça um programa que leia o sexo e o peso de 10 pessoas, e mostre quantas pessoas do sexo masculino possuem peso entre 60 e 80 kg, bem como a quantidade de mulheres que possuem peso entre 50 e 70 kg.
'''
qtd_pessoas = 10 
qtd_homem_peso = 0
qtd_mulher_peso = 0

for i in range(qtd_pessoas):
    sexo = input('Informe o sexo da pessoa (M ou F): ')
    peso = float('Informe o peso da pessoa: ')

    if sexo.lower() == 'M' and peso>=60 and peso <=80:
        qtd_homem_peso = qtd_homem_peso + 1

    if sexo.lower() == 'F' and peso>=50 and peso <=70:
        qtd_mulher_peso = qtd_mulher_peso + 1

print(f'Quantidade de homens com peso entrw 60 e 80 kg: {qtd_homem_peso}')
print(f'Quantidade d mulheres com peso entre 50 e 70 kg: {qtd_mulher_peso}')