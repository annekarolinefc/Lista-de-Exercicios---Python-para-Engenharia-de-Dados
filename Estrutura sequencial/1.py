'''
1.	Leia três números inteiros e imprima a média aritmética entre esses números.
'''

def media_aritmetica(num1, num2, num3):
    return ((num1+num2+num3)/3)

x = int(input('Digite o primeiro numero:'))
y = int(input('Digite o segundo numero:'))
z = int(input('Digite o terceiro numero:'))
print(f'Media => {round(media_aritmetica(x, y, z), 2)}')