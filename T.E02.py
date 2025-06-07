try:
    n1=int(input("Digite um número"))
    n2=int(input("Digite um número"))
    soma=n1/n2
    print(soma)
except ZeroDivisionError:
    n2=0
    print("Erro! Divida o número por outro que não seja 0")
except ValueError:
    print("Digite um NÚMERO")