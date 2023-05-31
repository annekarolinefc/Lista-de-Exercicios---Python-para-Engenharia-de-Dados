"""
Faça um programa que faça a leitura de 5 valores, e para cada valor, mostre o seu dobro na tela.
"""
valores = []
tentativas = 5
print('Insira 5 valores:')
for x in range(0, 5):
    num = float(input('Numero: '))
    valores.append(num)

for x in valores:
    print(f'O dobro de {x} => {x*2}')