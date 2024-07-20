valor1 = 0
valor2 = 0
menu = ""

valor1 = int (input('Digite o 1° valor: \n'))
valor2 = int (input('Digite o 2° valor: \n'))
while True:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5] Sair do programa')
    menu = int (input('Digite qual operação você deseja realizar com esses valores:  \n'))
    if menu == 1:
        print(valor1+valor2)

    elif menu == 2:
        print(valor1*valor2)

    elif menu == 3:
        print(max(valor1, valor2))

    elif menu ==4:
        valor1 = input('Digite o 1° valor: \n')
        valor2 = input('Digite o 2° valor: \n')

    elif menu == 5:
        print('Saiu')
        break

    else:
        print('Apenas uma das opções')