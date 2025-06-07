simulador=input("Digite um número de 1 a 5:")
match simulador:
    case "1":
        print("Pizza")
    case "2":
        print("Hambúrguer")
    case "3":
        print("Sushi")
    case "4":
        print("Salada")
    case "5":
        print("Lasanha")
    case _:
        print("Inválido")
