"""
crie funçoes que duplicam, triplicam, quadruplicam ...
o numero recebido como parametro
"""

# def multiplica(num_antes_operador, num_depois_operador):
#     return num_antes_operador * num_depois_operador

# num1, num2 = input("insira dois numeros para a multiplicaçao: ").split()

# resultado = multiplica(int(num1), int(num2))

# print(resultado)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar


duplicar = criar_multiplicador(2)
print(duplicar(4))