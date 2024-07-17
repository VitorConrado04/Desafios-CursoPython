#Programa criado para informar se uma pessoa precisa servir o exército, se ainda não precisa ou se já passou da idade.


anoN = int (input('Em que ano você nasceu? \n'))

if 2024 - anoN == 18:
    print('Você precisa se alistar ao exército')

elif 2024 - anoN > 18:
    print('Já passou da hora de você se alistar')

else:
    print('Você ainda não precisa se alistar ao exército')