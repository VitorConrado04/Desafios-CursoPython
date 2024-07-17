# Programa criado para exibir a soma de 6 números digitados pelo usuário.


soma = 0
for x in range (6):
    num = int (input('Digite um número: '))
    if num % 2==0:
        soma = soma + num

print(soma)

