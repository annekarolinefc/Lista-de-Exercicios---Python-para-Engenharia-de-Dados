""" 
1. Solicite ao usuário que digite uma frase. Imprima:
	- o tamanho (em caracteres) da frase
	- a frase toda em maiúscula
	- a frase toda em minúscula
	- a frase na vertical(letra por letra)
	- solicite ao usuário que informe uma posição inicial e final na frase, e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	- a frase em ordem inversa
	- solicite ao usuário que informe duas palavras. Substitua, na frase informada, a primeira palavra informada pelo usuário, pela segunda palavra informada. Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.
"""

frase = input('Insira uma frase: ')
print(f'Tamanho da frase: {len(frase)} caracteres')
print(f'Frase maisucula: {frase.upper()}')
print(f'Frase minuscula: {frase.lower()}')
print(f'Frase na vertical: ')
for letra in frase:
    print(letra)

posicao_inicial = int(input('Informe a posição inicial:'))
posicao_final = int(input('Informe a posição final:'))
print(f'Trecho da frase: {frase[posicao_inicial:posicao_final]}')
print(f'Frase invertida: {frase[::-1]}')

print('Informe duas palavras:')
primeira_palavra = input('Insira a primeira palavra:')
segunda_palavra = input('Insira a segunda palavra:')
nova_frase = frase.replace(primeira_palavra, segunda_palavra)
print(f'Nova frase: {nova_frase}')