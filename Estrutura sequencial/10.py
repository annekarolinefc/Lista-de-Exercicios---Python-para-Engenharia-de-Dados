'''
Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
'''

a = input('Insira uma variável (a): ')
b = input('Insira uma variável (b): ')
print(f'\nAs duas variaveis inseridas pelo usuario: {a} e {b}')
print(f'Trocando o conteúdos das variáveis...')
b, a = a, b 
print(f'As duas variaveis inseridas pelo usuario invertidas: {a} e {b}.\n')