#Programa criado para exibir um texto digitado pelo usuário através de recursos de manpulação de string.


nome = (input("Digite seu nome: \n"))
print(nome.upper())
print(nome.lower())
tamanho = (len(nome))
espacos = nome.count(' ')
print(tamanho-espacos)
print(nome.find(' '))
