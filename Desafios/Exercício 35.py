#Programa criado para verificar se com o comprimento de 3 retas digitadas pelo usuário é capaz de formar um triângulo.

ret1 = float (input('Digite o valor da 1 reta: '))
ret2 = float (input('Digite o valor da 2 reta: '))
ret3 = float (input('Digite o valor da 3 reta: '))
if ret1+ret2>ret3 and ret1+ret3>ret2 and ret2+ret3>ret1:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')