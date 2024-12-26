"""
higher order functions
funçoes de primeira classe
"""

def saudacao(msg, nome):
    return f"{msg}, {nome}!"


def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "bom dia", "luis")
print(v)
v = executa(saudacao, "bom dia", "julia")
print(v)
v = executa(saudacao, "bom dia", "nome aleatorio")
print(v)