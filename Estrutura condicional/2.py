'''
    Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
    >= 7 -> Aprovado
    < 7 -> Reprovado
'''
print('Insira as notas do aluno:')
nota1=input('Insira a primeira nota do aluno:')
nota2=input('Insira a segunda nota do aluno:')

def media(nota1, nota2):
    media = (nota1+nota2)/2
    if media>=7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
print(f'O aluno está: {media(nota1, nota2)}')