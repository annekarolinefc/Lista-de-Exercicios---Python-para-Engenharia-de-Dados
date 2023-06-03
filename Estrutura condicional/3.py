
'''
3. Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
- >= 0 e < 3 REPROVADO 
- >= 3 e < 7 EXAME 
- >= 7 e <= 10 APROVADO 
'''

print('Insira as notas do aluno:')
#nota1=input('Insira a primeira nota do aluno:')
#nota2=input('Insira a segunda nota do aluno:')
#nota3=input('Insira a terceira nota do aluno:')

def media(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    if ((media>=7) and (media<=10)):
        return 'APROVADO'
    elif ((media>=3) and (media<7)):
        return 'EXAME'
    elif ((media>=0) and (media<3)):
        return 'REPROVADO'
    
media = media(1, 2, 3)
print(media)