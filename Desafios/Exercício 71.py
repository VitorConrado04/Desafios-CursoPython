cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0
saque = int (input('Qual será o valor do saque? \n'))
while True:
    if saque>50:
        cedulas50 = saque//50
        saque%=50

    if saque>20:
        cedulas50 = saque//20
        saque%=20

    if saque>10:
        cedulas50 = saque//10
        saque%=10

    if saque>1:
        cedulas50 = saque//1
    print(f'A quantidade de notas de 50,00 R$ foi de: {cedulas50} nota/s')
    print(f'A quantidade de notas de 20,00 R$ foi de: {cedulas20} nota/s')
    print(f'A quantidade de notas de 10,00 R$ foi de: {cedulas10} nota/s')
    print(f'A quantidade de notas de 1,00 R$ foi de: {cedulas1} nota/s')
    sair = input('Deseja sair? (S/N)').upper()