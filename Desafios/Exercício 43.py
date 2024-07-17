#Programa criado para calcular o IMC do usuário e informar a sua condição de saúde com base no mesmo.


peso = float (input('Digite seu peso: '))
altura = float (input('Digite sua altura em centrímetros: '))
imc = peso / ((altura*altura) / 100)

if imc < 18.5:
    print('Abaixo do peso')

elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')

elif imc > 25 and imc <= 30:
    print('Sobrepeso')

elif imc > 30 and imc <= 40:
    print('Obesidade')

else:
    print('Obesidade mórbida')