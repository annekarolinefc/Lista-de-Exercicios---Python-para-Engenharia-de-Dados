""" 
2. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que digite uma palavra. Imprima uma mensagem informando a quantidade de vezes em que a palavra se encontra na frase (considere que a palavra pode estar em maiúscula ou minúscula na frase).
"""

frase = input('Insira uma frase: ')
palavra = input('Insira uma palavra: ')

ocorrencia = 0
frase_lista = frase.split(' ')
for elemento in frase_lista:
    if palavra.upper() == elemento.upper(): 
        ocorrencia = ocorrencia + 1
print(f'Ocorrencias da palavra {palavra.upper()} na frase {frase.upper()}: {ocorrencia}')