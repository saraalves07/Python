valor=input("Digite uma forma geométrica Triângulo, Quadrado ou Círculo:").capitalize()

match valor:
    case 'Triângulo':
        print("Você escolheu Triângulo")
    case 'Quadrado':
        print("Você escolheu Quadrado")
    case 'Círculo':
        print("Você escolheu Círculo")
    case _:
        print("Opção Inválida")
