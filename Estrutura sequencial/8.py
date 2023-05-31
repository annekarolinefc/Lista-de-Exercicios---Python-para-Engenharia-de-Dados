"""
Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
Peso ideal (P) = (72,7 * H) – 58. 
"""
h_homem = float(input('Insira a Altura de um homem (em metros):'))
peso_ideal = ((72.7 * h_homem) - 58)

print(f'O peso idel de um homem com {h_homem}m de altura => {round(peso_ideal, 2)}kg.\n')