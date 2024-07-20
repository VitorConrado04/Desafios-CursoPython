import random
numero = random.randint (0,10)
contador = 0
user = int (input('Digite um número de 1 a 10: \n'))
contador += 1
while user != numero:
    user = int (input('Número errado, tente novamente: \n'))

print(f'Número certo! A quantidade necessária de tentativas foi {contador}')