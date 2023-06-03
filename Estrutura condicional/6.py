'''
6 - Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
IMC= PESO/ALTURA2
e, a situação do peso é determinada pela tabela abaixo:

'''

def calcula_imc(peso, altura):
    imc = peso/(altura*altura)
    return imc

imc = calcula_imc(peso, altura)