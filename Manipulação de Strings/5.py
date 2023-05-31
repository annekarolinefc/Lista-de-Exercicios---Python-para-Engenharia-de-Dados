""" 
5. Solicite ao usuário que digite uma palavra e imprima uma mensagem informando se a palavra é ou não um palíndromo (uma palavra que se lê da mesma maneira nos dois sentidos. Por exemplo: OVO, RADAR, OSSO etc.)
"""
palavra = input('Digite uma palavra: ').upper().replace(' ', '' )
# notação de slice

print(palavra)
if palavra == palavra[::-1]:
    print(f'Palavra {palavra} é um palíndromo.')
else: 
    print(f'Palavra {palavra} não é um palíndromo.')
