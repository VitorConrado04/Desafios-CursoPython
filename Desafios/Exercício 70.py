# #Crie um programa que leia o nome e o preço de vários produtos. O
# programa deverá perguntar se o usuário vai continuar. No final,
# mostre:
#
# A) Qual é o total gasto na compra.
#
# B) Quantos produtos custam mais de R$ 100,00.
#
# C) Qual é o nome do produto mais barato.


total = 0
mc = 0
pf = 0
nome = input('Qual o nome do produto? \n')
pp = float (input ('Digite o valor do produto: \n'))
total += pp
valor_b = float ('inf')
nome_b = ''
if pp < valor_b:
    pf = pp
    nome_b = nome
if pp > 100:
    mc =+ 1
sn = input('Deseja cadastrar um novo produto? \n SIM \n NÃO\n').upper()
while sn == 'SIM':
    nome = input('Qual o nome do produto? \n')
    pp = float(input('Digite o valor do produto: \n'))
    total += pp
    valor_b = float('inf')
    nome_b = ''
    if pp < valor_b:
        pf = pp
        nome_b = nome
    if pp > 100:
        mc = + 1
    sn = input('Deseja cadastrar um novo produto? \n SIM \n NÃO\n').upper()

else:
    print('Produtos registrados.')


print(f'O total gasto na compra foi de {total} R$')
print(f'A quantidade de produtos que custam mais de 100,00 R$ é de {mc} produto/s')
print(f'O produto mais barato é {nome_b}')
