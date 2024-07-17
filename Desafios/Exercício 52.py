# Progama criado para verificar se um número digitado pelo usuário é ou não primo.


num = int (input('Digite um número inteiro: '))

if num % num == 0 and num % 1 == 0 and not num % (2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) == 0:
    print(f'O número {num} é primo')

else:
    print(f'O número {num} não é primo')
