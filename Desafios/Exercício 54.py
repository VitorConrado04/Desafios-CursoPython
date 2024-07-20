contador = 0

for c in range (7):
    idade = int (input('Digite seu ano de nascimento: '))
    idade = idade - 2024
    if idade>18:
        contador = contador + c
    else:
        contador

print(f'O número de pessoas maior de idade é {contador}')

