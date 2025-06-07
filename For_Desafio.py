import random
print("Adivinhe o número aleatório")
correto=random.randint(1,100)

while True:
    number=int(input("Digite aqui:"))
    if number==correto:
        print("Número Correto, Parabéns")
        break

    elif number> correto:
        print("Número incorreto, Digite um número menor!")

    else:
        print("Número incorreto, Digite um número maior!")
