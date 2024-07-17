#Exercício para verificação se um carro foi ou não multado baseado em um limite de velocidade, e se sim, de quanto foi a multa baseado em uma constante
# de 7 reais por KM/H excedido. 


velocidade = float (input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado!')
    if velocidade > 80:
        print (f'O valor da multa é de: {(velocidade - 80)*7} reais')
else:
    print('Você não foi multado!')