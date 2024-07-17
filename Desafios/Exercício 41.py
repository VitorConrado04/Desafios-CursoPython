#Programa criado para ler o ano de nascimento de uma pessoa e informar a qual categoria etária ela pertence.


ida = 2024 - int (input('Digite seu ano de nascimento: '))

if ida < 9:
    print('Mirim')

elif ida >= 9 and ida <= 14:
    print('Infantil')

elif ida > 15 and ida <= 19:
    print('Junior')

elif ida> 19 and ida<=24:
    print('Sênior')

else:
    print('Master')