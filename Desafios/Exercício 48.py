#Programa criado para ler a soma dos números de uma sequência.


soma=0
for tres in range (1,501):
    if tres % 3 == 0 and tres%2==1:
        soma += tres

print(f'A soma de todos os números é {soma}')