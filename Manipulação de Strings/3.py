""" 
3. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que informe um caractere de maneira que a frase seja dividida em partes de acordo com o caractere informado. Imprima na tela a frase dividida.
"""
frase = input('Insira uma frase: ')
caracter = input('Insira um caracter divisor: ')
frase_dividida = frase.split(caracter)
print(f'Frase dividida por {frase_dividida}: ')