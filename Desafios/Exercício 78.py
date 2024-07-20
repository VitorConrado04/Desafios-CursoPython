#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

maior = 0
menor = 0
lista = []
contador = 0
num = int (input('Digite um valor númerico: '))
lista.append(num)
contador += 1
while contador < 5:
    num = int(input('Digite um valor númerico: '))
    lista.append(num)
    contador += 1

lista.sort()
maior = lista [-1]
menor = lista [0]
print(f'O maior valor da lista foi {lista [-1]} a posição é a {lista.index(maior)}')
print(f'O menor valor da lista foi {lista [0]} a posição é a {lista.index(menor)}')
