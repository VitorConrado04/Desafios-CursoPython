#Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

#Ao final, mostre o conteúdo das três listas geradas.

num = 0
confirma = ''
lista = []
par = []
impar = []

num = int (input('Digite um número inteiro: \n'))
lista.append(num)
if num%2==0:
    par.append(num)

else:
    impar.append(num)
confirma = input('Deseja digitar outro número? \nSIM\nNÃO\n').upper()

while confirma == 'SIM':
    num = int(input('Digite um número inteiro: \n'))
    lista.append(num)
    confirma = input('Deseja digitar outro número? \nSIM\nNÃO\n').upper()
    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

print(f'Segue a seguir a lista com todos os números: {lista} \n')
print(f'Segue a seguir a lista com os números pares: {par} \n')
print(f'Segue a seguir a lista com os números ímpares: {impar} \n')

