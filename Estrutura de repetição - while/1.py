'''
1 - Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. 
O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa. 
'''

print('Informe a matrícula e as três notas de um conjunto de alunos:')
matricula = input('Matricula: ')
nota1 = input('Nota1:')
nota2 = input('Nota2:')
nota3 = input('Nota3:')
media = (nota1+nota2+nota3)/3
exame = False 

