# Programa para calcular um possível financeamento de uma casa com base no seu valor, na quantidade de anos da dívida pretendida e o
# salário do possível comprador. 


casa = float (input('Qual o valor da casa? '))
sal = float (input('Quaal o valor do seu salário? '))
anos = int (input('Em quantos anos você pretende pagar?'))

prestação = casa / (anos * 12)

if prestação > sal * 0.30:
    print('A prestação excederá 30% do seu salário.')
else:
    print(f'A prestação vai ser de: {prestação: ,.2f}')