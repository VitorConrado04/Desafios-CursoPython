#Programa de jogo de par ou ímpar com PC que se repete enquanto o jogador ganhar.


import random

contador = 0
while True:
    pi = input('Escolha par ou ímpar: \n').lower()
    pc = random.randint (0,10)
    user = int (input('Digite um número para jogar par ou ímpar contra o PC: \n'))


    if pi == 'par':
        if (user + pc)%2==0:
            contador = contador + 1
            print('Você ganhou!')

        else:
            print(f'Você perdeu, o número escolhido pelo PC foi {pc}')
            break

    if pi == 'impar':
        if (user + pc)%2==1:
            contador = contador + 1
            print('Você ganhou!')

        else:
            print(f'Você perdeu, o número escolhido pelo PC foi {pc}')
            break

print(f'A quantidade de vitórias seguidas foi de {contador}')

