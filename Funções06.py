def valor(operadores, N1, N2):
    match operadores:
        case "Adição"|"adição"|"+":
            resultado=N1+N2
            print(resultado)
        case "Subtração"|"subtração"|"-":
            resultado=N1-N2
            print(resultado)
        case "Multiplicação"|"multiplicação"|"*":
            resultado=N1*N2
            print(resultado)
        case "Divisão"|"divisão"|"/":
            resultado=N1/N2
            print(resultado)
        case _:
            print("Vai dar não")

nomes=input("Digite o seu nome:")
Digite=input(f"Bem-vindo(a) {nomes}! Digite a operação desejada para começarmos:")
N1=int(input("Digite o número:"))
N2=int(input("Digite o outro número:"))

valor(Digite, N1, N2)



    


