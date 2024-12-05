primeiro_valor = input("Insira um valor: ")
segundo_valor = input("Insira um valor: ")

if primeiro_valor >= segundo_valor:
    print(
        f"O {primeiro_valor = } é maior ou igual" 
        f" ao {segundo_valor = }"
    )
else:
    print(
        f"O {segundo_valor = } é maior"
        f" que o {primeiro_valor = }"
    )