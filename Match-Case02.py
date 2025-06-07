number=input("Digite um número de 0 a 10:")

match number:
    case "9"|"10":
        print("Excelente")
    case "7"|"8":
        print("Bom")
    case "5"|"6":
        print("Regular")
    case "3"|"4":
        print("Ruim")
    case "0"|"1"|"2":
        print("Muito ruim")