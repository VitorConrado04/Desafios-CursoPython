#Programa criado para verificar quanto custará uma viagem com base nas constantes que uma viagem menor que 200KM tem a taxa de 0.5 a cada KM
# e sendo uma viagem maior que 200KM a taxa de 0.45 será aplicada.

viagem = float (input('De quantos KM é a viagem? \n'))
if viagem <= 200:
    print(f'A sua viagem custará: {viagem*0.5}')
else:
    print (f'A sua viagem custará: {viagem*0.45}')