#Mini jogo criado com a biblioteca random em que o usuário tenta acertar um número pensado pelo computador.

import random
numero = random.randint (0,5)
user = int (input('Digite um número de 1 a 5: \n'))
if user == numero:
    print('Você acertou o número!')
else:
    print('Você errou o número T-T')

print(f'O número pensado pelo computador foi: {numero}')

#Operador ternario funciona com duas condições de if e else print ('texto' if condição else)
