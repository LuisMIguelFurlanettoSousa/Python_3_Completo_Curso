while True:

    n1 = input("Digite o primeiro numero: ")
    n1_inteiro = int(n1)

    operador = input("Digite o operador (+, -, *, /): ")

    n2 = input("Digite o segundo numero: ")
    n2_inteiro = int(n2)

    if operador == '+':
        resultado = n1_inteiro + n2_inteiro
        print(f"{n1_inteiro} + {n2_inteiro} = {resultado}")
    elif operador == '-':
        resultado = n1_inteiro - n2_inteiro
        print(f"{n1_inteiro} - {n2_inteiro} = {resultado}")
    elif operador == '*':
        resultado = n1_inteiro * n2_inteiro
        print(f"{n1_inteiro} * {n2_inteiro} = {resultado}")
    elif operador == '/':
        resultado = n1_inteiro / n2_inteiro
        print(f"{n1_inteiro} / {n2_inteiro} = {resultado:.2f}")
    else:
        print("Reposta invalida")

    sair = input("Deseja sair? [S]im: ")
    sair = sair.lower()
    sair = sair.startswith("s")

    if sair:
        break

