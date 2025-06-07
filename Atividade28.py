n1=float(input("Primeira nota:"))
n2=float(input("Segunda nota:"))
n3=float(input("Terceira nota:"))
n4=float(input("Quarta nota:"))

media=(n1+n2+n3+n4)/4

if media >=6:
    print("aee, passou")
elif media <6 and media>4:
    print("Recuperação")
else:
    print("reprovado")