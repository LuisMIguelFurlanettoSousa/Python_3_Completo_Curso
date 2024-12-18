"""
args - Argumentos nao nomeados 
* - *args (empacotamento e desempacotamento)
"""

# x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total

# soma_1_2_3 = soma(1, 2, 3)
# #print(soma_1_2_3)

# outra_soma = soma(1, 5166, 1616, 1, 8)
# #print(outra_soma)

numeros = 1, 2, 3, 4, 5
print(soma(*numeros))