#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
# No final serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = []
num = int (input('Digite um valor númerico: \n'))
lista.append(num)
lista.sort()
confirmacao = input('Você deseja digitar outro valor?\n SIM\n NÃO\n').lower()
while confirmacao == 'sim':
    num = int(input('Digite um valor númerico: \n'))
    while num in lista:
        num = int (input('Número já presente na lista, tente outro: \n'))
    else:
        lista.append(num)
        lista.sort()
        confirmacao = input('Você deseja digitar outro valor?\n SIM\n NÃO\n').lower()


print(lista)