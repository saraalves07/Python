try:
    n1=float(input("Digite um número: "))
    n2=float(input("Digite um número: "))
    n3=float(input("Digite um número: "))
    n4=float(input("Digite um número: "))
    resultado=n1+n2+n3+n4/4
    print(resultado)
except ValueError:
    print("Deu erro aqui ó! Arruma isso daí")
