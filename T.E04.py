try:
    valor=float(input("Digite sua idade: "))
    if valor>=18:
        print("Autorizado com sucesso!")
    else:
        print("Não Autorizado")
except ValueError:
    print("Valor Inválido")