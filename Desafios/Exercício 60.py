fatorial = 1
num = int (input('Digite um número inteiro: \n'))
while num > 1:
    fatorial *= num
    print(num, end=' x ')
    num -= 1
print(fatorial)

