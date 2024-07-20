#Programa criado para ler várias vezes um número inteiro pelo teclado
#até o valor "999" ser digitado. No final também temos que informar quantos
#números foram digitados e qual a soma deles.


contador = 0
num = int (input('Digite um número inteiro: \n'))
contador = contador + 1

while num != 999:
    num += int (input('Digite um número inteiro: \n'))

print('Você digitou o número para encerrar o programa.')
print(f'A quantidade de tentativas foi de {contador} tentativas ')