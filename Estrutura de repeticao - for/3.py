'''
Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''
def tabuada(numero):
    return f'''
        {numero}x1 = {numero*1} 
        {numero}x2 = {numero*2}  
        {numero}x3 = {numero*3}  
        {numero}x4 = {numero*4}  
        {numero}x5 = {numero*5}  
        {numero}x6 = {numero*6}  
        {numero}x7 = {numero*7}  
        {numero}x8 = {numero*8}  
        {numero}x9 = {numero*9}  
        {numero}10 = {numero*10} 
    '''
    
num = int(input('Insira um numero para imprimir sua tabuada:'))
result = tabuada(num)
print(result)