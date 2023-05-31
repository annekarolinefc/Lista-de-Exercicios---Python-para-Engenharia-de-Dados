""" 
4. Solicite ao usuário que digite uma palavra. Em seguida, solicite ao mesmo que informe um caractere separador, de maneira que o separador seja incluído na palavra, separando cada letra da palavra digitada. 
"""
palavra = input('Digite uma palavra: ')
separador = input('Informe o separador desejado: ')
resultado = separador.join(palavra)

print(f'O resultado será: {resultado}\n')