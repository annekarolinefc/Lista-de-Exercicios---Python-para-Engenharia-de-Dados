'''
9 - Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
- não eleitor (abaixo de 16 anos); 
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos); 
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)

'''
def classe_eleitora(idade):
    if idade<16:
        return 'Não eleitor'
    elif idade>=18 and idade<65:
        return 'Eleitor Obrigatório'
    elif (idade>=16 and idade<18) or idade>=65:
        return 'Eleitor facultativo'