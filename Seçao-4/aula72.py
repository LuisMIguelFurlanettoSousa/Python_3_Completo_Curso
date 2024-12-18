# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for n in args:
        n = int(n)
        total *= n
        
    def par_impar(num):
        if num % 2 == 0:
            return "par"
        else:
            return "impar"

    numero = par_impar(total)
    return total, numero

resultado_multi, verifica= multiplica(*input("Insira numeros: ").split())

print(resultado_multi, verifica)