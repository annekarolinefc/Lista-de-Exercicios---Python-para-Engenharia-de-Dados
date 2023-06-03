'''
    1- Faça um programa que receba dois números e mostre o maior e o menor. 
    Emita uma mensagem, caso os dois sejam iguais.
'''

import unittest

def testaNumero(num1, num2):
    """Return ....."""
    if num1>num2:
        return f'{num1} maior que {num2}.'
    elif num2>num1:
        return f'{num2} maior que {num1}.'
    else:
        return f'Os numeros sao iguais: {num1} e {num2}.'
 
class Exercice1TestCase(unittest.TestCase):
    def testa2maiorque1(self):
        """Tests for 1.py."""
        numero = testaNumero(1, 2)       
        self.assertEqual(numero, '2 maior que 1.')
        
    def testa1maiorque2(self):
        """Tests for 1.py."""
        numero = testaNumero(2,1)       
        self.assertEqual(numero, '2 maior que 1.')
        
    def testa2iguala2(self):
        """Tests for 1.py."""
        numero = testaNumero(2,2)       
        self.assertEqual(numero, 'Os numeros sao iguais: 2 e 2.')
unittest.main()