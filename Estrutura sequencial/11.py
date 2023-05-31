'''
Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato. Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.
'''
a = int(input('Insira o numero total de eleitores: '))
can_1 = int(input('Insira o número de votos do primeiro candidato: '))
can_2 = int(input('Insira o número de votos do segundo candidato: '))
nulos = a - can_1 - can_2
print(f'\nExibindo o percentual de votos de cada um dos candidados e o percentual de votos nulos')
print(f'Candidado 1: {(can_1/a)*100}%')
print(f'Candidado 2: {(can_2/a)*100}%')
print(f'Nulos: {(nulos/a)*100}%\n')