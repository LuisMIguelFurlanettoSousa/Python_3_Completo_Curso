# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }



# print(pessoa)

# print()

# print(pessoa["nome"])
# print(pessoa['altura'])

# print()

# for key in pessoa:
#     print(key, pessoa[key])

# pessoa = {}

# key = "nome"

# pessoa[key] = "Luis Miguel" 
# pessoa["sobrenome"] = "Furlanetto"

# print(pessoa[key])

# pessoa[key] = "Julia"
# #del pessoa["sobrenome"]

# print(pessoa)

# if pessoa.get("sobrenome") is not None:
#     print(pessoa["sobrenome"])
# else:
#     print("NAO existe")

# -------------------------------------------------

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 89,
    'l1': [1, 2, 4],
}


# pessoa.setdefault("idade", 0) #se nao existir a key idade ele define ela como 0
# print(pessoa["idade"])
# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# pessoa2 = copy.deepcopy(pessoa)

# pessoa2["nome"] = "Julia"
# pessoa2["l1"][1] = 9999999999999999
# print(pessoa)
# print(pessoa2)

#print(pessoa.get("nome")) #se a key nao existir retorna None

# nome = pessoa.pop("nome")
# print(nome)
# print(pessoa)

# ultima_chave = pessoa.popitem() #deleta o ultimo item do dict

# print(ultima_chave)

# pessoa.update({
#     "nome": "Julia amor da minha vida",
#     "altura": "baixa"
# })

# pessoa.update(nome="julia amor da minha vida", altura="baixa")

tupla = ("nome", "novo valor"),
pessoa.update(tupla)

print(pessoa)