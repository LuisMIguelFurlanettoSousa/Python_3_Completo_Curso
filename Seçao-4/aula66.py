"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definiçao
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', "x + y + z=", x + y + z)

soma(1, 2, 3)# argumento nao nomeado
soma(y=2, z=3, x=1) # argumento nomeado
soma(1, 2, z=3)