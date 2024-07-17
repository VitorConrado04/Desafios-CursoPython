# Programa para exibir a tabuada de um número até o muliplicador 10. 


num = int (input('Digite um número para ver a tabuada: '))

for tabuada in range (num, (num * 11) ,num):
    print(tabuada)