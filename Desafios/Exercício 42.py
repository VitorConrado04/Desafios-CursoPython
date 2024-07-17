# Programa para ler o comprimento de 3 retas digitados pelo usuário, informar se com as mesmas é possível ou não formar um triângulo com essas retas
# e qual tipo de triângulo será formado.


ret1 = float (input('Digite o valor da 1 reta: '))
ret2 = float (input('Digite o valor da 2 reta: '))
ret3 = float (input('Digite o valor da 3 reta: '))
if ret1+ret2>ret3 and ret1+ret3>ret2 and ret2+ret3>ret1:
    print('As retas podem formar um triângulo')
    if ret1 == ret2 == ret3:
        print('O triangulo formado será o equilátero')
    elif ret1 == ret2 or ret1==ret3 or ret2==ret3:
        print('O triangulo formado será o isósceles')

    else:
        print('O triangulo formado será o Escaleno')
else:
    print('As retas não podem formar um triângulo')

