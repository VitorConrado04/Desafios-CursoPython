#Programa criado para ler duas notas e informar se um alúno foi reprovado, aprovado ou se encontra em recuperção com base na média ser de 5.


not1 = float (input('Digite a primeira nota: '))
not2 = float (input('Digite a segunda nota: '))

if (not1 + not2) / 2< 4.9:
    print('Reprovado')

elif (not1 + not2) / 2 > 5.0 and (not1 + not2) / 2 < 6.0:
    print('Recuperação')

else:
    print('Aprovado')