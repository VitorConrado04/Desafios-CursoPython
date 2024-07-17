#Programa criado para exibir o valor total da prestação de um produto e o valor das prestações mensais com base em valores inseridos pelo usuário.

valor = float (input("Digite o valor do produto comprado: "))
taxa = float (input("Digite o valor da taxa desse produto: "))
tempo = int (input("Em quantas prestações foi a compra? "))
print("O valor da prestação total é de: ", valor + (valor * (taxa/100))*tempo)
print("O valor das prestações com base no tempo será de: ", valor + (valor * (taxa/100))*tempo/tempo)
