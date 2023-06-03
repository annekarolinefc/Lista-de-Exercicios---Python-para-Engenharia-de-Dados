'''
4-Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
'''
#x, y, z = (1, 2, 3)

w = int(input('Insire um lado do triângulo: '))
y = int(input('Insire um lado do triângulo: '))
z = int(input('Insire um lado do triângulo: '))

def ehtriangulo(x, y, z):
    if (x<(y+z)) and (y<(x+z)) and (z<(x+y)):
        return True
    else:
        return False
    
triangulo = ehtriangulo(w, y, z)
print(triangulo)

if triangulo == True:
    print('Os lados formam um triangulos.')
else:
    print('Os lados nao formam um triangulos.')