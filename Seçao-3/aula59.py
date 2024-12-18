# desempacontamento em camadas
# de metodos e funçoes

string = "ABCD"
lista = ["Maria", "helena", 1, 2, 3, "Eduarda"]
tupla = "python", "é", "legal"
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 4)],  # 2
]

# p, b, *_, ap, u = lista
# print(p, ap, u)

# for nome in lista:
#     print(nome, end=" ")

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep="\n")