'''
    Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
    >= 7 -> Aprovado
    < 7 -> Reprovado
'''

import unittest

def media(nota1, nota2):
    media = (nota1+nota2)/2
    if media>=7:
        return 'Aprovado'
    else:
        return 'Reprovado'

class Exercice2TestCase(unittest.TestCase):
    def testaAprovado(self):
        """Tests for 2.py."""
        mediaAluno = media(9, 9)       
        self.assertEqual(mediaAluno, 'Aprovado')
    def testaReprovado(self):
        """Tests for 2.py."""
        mediaAluno = media(5, 5)       
        self.assertEqual(mediaAluno, 'Reprovado')
unittest.main()