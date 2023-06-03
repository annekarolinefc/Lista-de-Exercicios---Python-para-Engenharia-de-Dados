""" 
    2.	Leia a matrícula e a nota de 5 alunos da disciplina Python para Engenharia de Dados. Armazene-os em um dicionário. Imprima:
    a.	A média das notas
    b.	O(s) aluno(s) que obtiveram a maior nota
    c.	O(s) aluno(s) que obtiveram a menor nota

"""
cont = 0
alunos = {}
while cont <=5:
    matricula = input('Insira a matricula do aluno:')
    nota = float(input('Insira a nota do aluno:'))
    alunos[matricula] = nota
    cont = cont + 1
    
#a.	A média das notas
media = sum(alunos.values())/len(alunos)
print(f"Media das notas dos alunos: {media}")
#b.	O(s) aluno(s) que obtiveram a maior nota
maior_nota = max(alunos.values())
for maior_nota in alunos.values():
    print(f'Aluno com maior nota: {alunos.keys()}')
#c.	O(s) aluno(s) que obtiveram a menor nota
menor_nota = min(alunos.values())