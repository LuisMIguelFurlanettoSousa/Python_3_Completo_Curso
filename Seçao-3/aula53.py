
#     [(0, 'Maria'), (1, 'hellen'), (2, 'Luis'), (3, 'joao')]
lista = ["Maria",       "hellen",      "Luis"]
lista.append("joao")

# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)

# mesma coisa que o for de cima
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for item in enumerate(lista):
#     print("For da tupla: ")
#     for valor in item:
#         print(f"\t{valor}")