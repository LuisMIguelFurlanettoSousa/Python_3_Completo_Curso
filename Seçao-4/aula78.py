# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = {'Luiz', 1, 2, 3, 3, 3, 3, 1}
# print(s1)

# lista = ["luis", "julia", 1, 2, 3, 3, 3, 3, 1]
# lista_set = set(lista)
# print(lista_set)
# l2 = list(lista_set)
# print(l2)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add("luis")
# s1.add(1)
# s1.update(("hello, world", 1, 3, 4, 5, 5, 5))
# #s1.clear()
# s1.discard("hello, world")
# s1.discard("luis")
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 5, 4}

# s4 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
s3 = s1 ^ s2
s1 = list(s1)
s2 = list(s2)
s1.extend(s2)
print(s3)