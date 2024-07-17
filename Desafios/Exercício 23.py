#Programa criado para ler um número digitado pelo usuário (Em formato de Str) e mostrar as informações sobre as casas decimais posteriomente. 


numero = str (input('Digite um número de 0 a 9999: \n'))
divideNumeroU = numero[3]
divideNumeroD = numero[2]
divideNumeroC = numero[1]
divideNumeroM = numero[0]

print('Unidade: ', divideNumeroU)
print('Dezena: ', divideNumeroD)
print('Centena: ', divideNumeroC)
print('Milhar: ', divideNumeroM)
