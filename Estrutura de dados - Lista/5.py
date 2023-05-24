""" 
5.	Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
1/11/2022 – 08 de novembro de 2022
(dica: crie uma lista contendo o nome de cada mês do ano)
"""

data = input('Digite uma data no formato DD/MM/AAAA: ')
mes_lista = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' ]

dia = data.split('/')[0]
mes = data.split('/')[1]
ano = data.split('/')[2]
# dia, mes, ano = data.split('/')

print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}\n')

print(f'{dia}/{mes}/{ano} - {dia} de {mes_lista[int(mes)-1]} de {ano}\n')