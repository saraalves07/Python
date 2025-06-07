senha=input("Insira a senha:")
correta='senha123'
while senha!=correta:
    print("Senha incorreta")
    senha=input("Insira a senha:")

    if senha==correta:
        print("Senha correta")
        break