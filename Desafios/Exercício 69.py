# Crie um programa que leia a idade e o sexo de varias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar. No final, mostre:
#
# A) Quantas pessoas tem mais de 18 anos.
#
# B) Quantos homens foram cadastrados.
#
# C) Quantas mulheres tem menos de 20 anos.


cot_maior = 0
cot_h = 0
cot_m = 0

idade = int (input('Digite sua idade: \n'))
if idade >= 18:
    cot_maior += 1

sexo = input('Digite seu sexo: \n MASCULINO \n FEMININO\n').upper()
if sexo == 'MASCULINO':
    cot_h += 1

if sexo == 'FEMININO' and idade < 20:
    cot_m += 1

cn = input('Você deseja cadastrar uma nova pessoa? \n SIM \n NÃO\n').upper()

while cn == 'SIM':
    idade = int(input('Digite sua idade: \n'))
    if idade >= 18:
        cot_maior += 1

    sexo = input('Digite seu sexo: \n MASCULINO \n FEMININO\n').upper()
    if sexo == 'MASCULINO':
        cot_h += 1

    if sexo == 'FEMININO' and idade < 20:
        cot_m += 1

    cn = input('Você deseja cadastrar uma nova pessoa? \n SIM \n NÃO\n').upper()
else:
    print('Programa encerrado.\n')

print(f'A quantidade de pessoas cadatradas com mais de 18 anos foi de {cot_maior} pessoas')
print(f'A quantidade de homens cadastrados no sistema foi de {cot_h} homens')
print(f'A quantidadede de mulheres com menos de 20 anos cadastradas no sistema foi de {cot_m} mulheres')