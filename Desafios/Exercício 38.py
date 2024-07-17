#Programa para ler dois valores digitados pelo usuário e informar, qual o maior, qual o menor e se eles são iguais.


num1 = int (input('Digite o primeiro valor: '))
num2 = int (input('Digite o segundo valor: '))

if num1>num2:
    print(f'O número {num1} é maior que o {num2}')

elif num1 == num2:
    print(f'O número {num1} é igual ao {num2}')

else:
    print(f'O {num2} é maior que o {num1}')