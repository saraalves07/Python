desafio=input("Escreva uma palavra:")
if desafio == desafio[::-1]:
    print("É um palíndromo") #Palíndromo é quando a palavra é a mesma coisa de trás pra frente. Ex:ana
else:
    print("Não é um palíndromo")