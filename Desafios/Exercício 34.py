#Programa que lê o salário do usuário e informa o quanto foi aumento baseado na condição de que se for maior que 1250 o aumento será de 10%
# e se for menor terá o aumento de 15%.

sal = float (input('Informe seu salário: '))
if sal > 1250:
    print(f'O aumento do salário foi de: {sal*0.10}')
else:
    print(f'O aumento do seu salário foi de: {sal*0.15}')
