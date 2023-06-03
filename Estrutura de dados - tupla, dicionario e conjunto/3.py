""" 
    3.	Crie um dicionário e armazene o nome e e-mail de 5 pessoas informados por você. Em seguida, solicite ao usuário que informe um nome. Imprima o e-mail da pessoa informada, caso exista no dicionário. Caso não exista, emita uma mensagem.
    Utilize a mesma estratégia para um e-mail informado pelo usuário.

"""

alunos = {3035: 'Alexandre', 8965: 'Maria', 7674: 'Carlos', 6758: 'Lucas'}

for RA, nome in alunos.items():
    print('RA:', RA, 'nome:', nome)
search = 'alexandre'
print('Procurando Alexandre...')
for RA, nome in alunos.items():
    if (search.lower() == nome.lower()):
        print('RA:', RA, 'nome:', nome)
        
pessoas = results = [
    {"nome": "Luiz",
    "email": "luiz@dominio.com.br"},
    {"nome": "Luiz",
    "email": "luiz@dominio.com.br"},
    {"nome": "Luiz",
    "email": "luiz@dominio.com.br"},
    {"nome": "Luiz",
    "email": "luiz@dominio.com.br"},
    {"nome": "Luiz",
    "email": "luiz@dominio.com.br"}
]

pessoa_input = input('Digite um nome: ')
if pessoa_input in pessoas:
    print(f'{pessoas.values()})