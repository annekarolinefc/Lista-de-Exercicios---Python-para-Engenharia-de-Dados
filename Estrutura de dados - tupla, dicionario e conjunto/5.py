""" 
    5.	Acesse o conteúdo JSON disponível em https://jsonplaceholder.typicode.com/posts e o armazene em uma lista Python. Baseado nesses dados, imprima na tela os títulos e os posts somente do usuário de userId = 10.
"""

import requests
import json 

url = 'https://jsonplaceholder.typicode.com/posts'
request = requests.get(url)

posts = json.loads(request.text) #objeto python
    
for post in posts:
    if post['userId']==10:
        print('Título: ', post['title'])
        print('Posts: ', post['body'], '\n')
    else:
        continue