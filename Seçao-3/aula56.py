"""
split e join com list e str

split - divide uma string
join - une uma string
strip- corta os espaços do cmc e do fim
rstrip - corta os epaços da direita
lstrip - corta os espaços da esquerda
"""

frase =  "   oha só que  ,  coisa interessante   "
lista_frases_cruas = frase.split(",")

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frase_unidas = ', '.join(lista_frases)
print(frase_unidas)