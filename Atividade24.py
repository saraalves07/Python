print("A primeira letra é maiúscula? Vamos ver!")
nome=input("Digite sua palavra:")
nome_capitalizado=" "
if nome==nome.capitalize():
    print("Você acertou!")
else:
    nome_capitalizado=nome.capitalize()


print(nome_capitalizado)