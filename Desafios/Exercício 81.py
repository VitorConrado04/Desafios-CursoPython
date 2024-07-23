# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#
# 	A) Quantos números foram digitados.
# 	B) A lista de valores, ordenada de forma decrescente.
# 	C) Se o valor 5 foi digitado e esta ou não na lista.


num = 0
lista = []
conf = ''
contador = 0

num = int (input('Digite um número: \n'))
lista.append(num)
lista.sort()
contador += 1
conf = input('Você deseja digitar outro número? \nSIM\nNÃO\n').upper()
while conf == 'SIM':
    num = int(input('Digite outro número: \n'))
    lista.append(num)
    lista.sort()
    contador += 1
    conf = input('Você deseja digitar outro número? \nSIM\nNÃO\n').upper()

else:
    lista.reverse()
    print(f'A quantidade de números digitados foi de {contador} números.\n')
    print(f'Os valores ordenados de maneira decrescente são: {lista}\n')
    if 5 in lista:
        print('O número 5 foi digitado na lista!')
    else:
        print('O número 5 NÃO foi digitado na lista!')
