'''
Faça o mesmo programa do item anterior, utilizando a fórmula para o cálculo do peso ideal para mulheres:
Peso ideal (P) = (62,1 * H) – 44,7
'''

h_mulher = float(input('Insira a Altura de uma mulher (em metros):'))
peso_ideal = ((62.1 * h_mulher) - 44.7)

print(f'O peso idel de um homem com {h_mulher}m de altura => {round(peso_ideal, 2)}kg.\n')