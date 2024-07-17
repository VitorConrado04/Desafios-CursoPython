#Programa criado para verficar o preço de um produto baseado na sua forma de pagamento.


preco = float (input('Digite o preço do produto: '))
pag = int (input('Digite a forma de pagamento:'
            '1 - A VISTA NO DINHEIRO // 2 - A VISTA NO CARTÃO // 3 - EM ATÉ 3 VEZES NO CARTÃO // 4 - 3X NO CARTÃO'))
if pag == 1:
    print(f'O valor pago a vista no dinheiro será de: {preco - preco*0.10}')

elif pag == 2:
    print(f'O preço a pagar a vista no cartão será de: {preco - preco*0.5}')

elif pag ==3:
    print(f'O valor pago em duas vezes no cartão será de: {preco}')

else:
    print(f'O valor pago em três vezes ou mais no cartão será de: {preco + 0.20}')
