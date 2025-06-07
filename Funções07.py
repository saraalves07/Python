def media():
    N1=int(input("Digite o primeiro número:"))
    N2=int(input("Digite o segundo número:"))
    N3=int(input("Digite o terceiro número:"))
    P1=int(input("Digite o peso um:"))
    P2=int(input("Digite o peso dois:"))
    P3=int(input("Digite o peso três:"))

    SomaPeso=P1+P2+P3
    resultado=N1*P1+N2*P2+N3*P3
    
    print(resultado/SomaPeso)
media()
    



