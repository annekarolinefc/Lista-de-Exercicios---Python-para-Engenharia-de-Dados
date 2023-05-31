'''
Faça um programa que leia a idade e peso de sete pessoas. Calcule e mostre:
	- a quantidade de pessoas com mais de 90 kg
	- a média das idades das sete pessoas
 '''
qtd_pessoas = 7
qtd_mais_90kg = 0
soma_idades = 0 
 
for i in range(qtd_pessoas):
    idade = int(input('Informe a idade da pessoa:'))
    peso = float(input('Informe o peso da pessoa:'))

    soma_idades = soma_idades + idade
    if peso > 90:
        qtd_mais_90kg = qtd_mais_90kg + 1

media_idades = soma_idades / qtd_pessoas

print(f'Quantidade de pessoas com mais de 90kg: {qtd_pessoas}')
print(f'Media das idades: {round(media_idades, 2)}')