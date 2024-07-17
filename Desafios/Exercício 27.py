#Programa criado para exibir o primeiro e o último nome digitado pelo usuário.

nome = input('Digite seu nome completo: ')
textoNome = nome.split()
print (f'O primeiro nome é: {textoNome [0] }')
print (f'O último nome é: {textoNome [-1] }')



