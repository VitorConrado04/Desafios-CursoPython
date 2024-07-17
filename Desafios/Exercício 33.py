#Programa criado para ler três números e exibir as informações sobre o maior e o menor deles.


n1 = float (input('Digite o primeiro número: '))
n2 = float (input('Digite o segundo número: '))
n3 = float (input('Digite o terceiro número: '))
if n1 > n2 > n3:
    print(f'O número {n1} é maior e {n3} é o menor número')

if n1 > n3 > n2:
    print(f'O número {n1} é o maior e o menor é {n2}')

if n2 > n1 > n3:
    print(f'O maior número é {n2} e o menor é {n3}')

if n2 > n3 > n1:
    print(f'O maior número é {n2} e o menor é {n1}')

if n3 > n1 > n2:
    print(f'O maior número é {n3} e o menor é {n2}')

#Else usado pois todas as outras condições já foram testadas, e se nenhuma retornou um valor verdadeiro só pode ser essa

else:
    print(f'O maior número é {n3} e o menor é {n1}')
