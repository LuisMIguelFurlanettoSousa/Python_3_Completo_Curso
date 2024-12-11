while True:

    n1 = input("Digite o primeiro numero: ")

    operador = input("Digite o operador (+, -, *, /): ")

    n2 = input("Digite o segundo numero: ")

    numeros_validos = None

    try:
        n1_float = float(n1)
        n2_float = float(n2)   

        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os numeros sao invalidos")
        continue


    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
        
    if operador == '+':
        resultado = n1_float + n2_float
        print(f"{n1_float} + {n2_float} = {resultado}")

    elif operador == '-':
        resultado = n1_float - n2_float
        print(f"{n1_float} - {n2_float} = {resultado}")

    elif operador == '*':
        resultado = n1_float * n2_float
        print(f"{n1_float} * {n2_float} = {resultado}")
        
    elif operador == '/':
        resultado = n1_float / n2_float
        print(f"{n1_float} / {n2_float} = {resultado:.2f}")
    
    else:
        print("Nunca deveria chegar aqui, ???")

    sair = input("Deseja sair? [S]im: ").lower().startswith("s")

    if sair:
        break
