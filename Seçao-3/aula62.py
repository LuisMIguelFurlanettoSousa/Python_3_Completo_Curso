"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf = input()
cpf_conta = cpf.replace('.', '').replace('-', '')
numeros_1 = []

for c in range(9):
    n = int(cpf_conta[c])
    numeros_1.append(n)

multiplicar_1 = 10
soma_numeros_1 = 0

for numero in numeros_1:
    soma_numeros_1 += numero * multiplicar_1
    multiplicar_1 -= 1

primeiro_numero = (soma_numeros_1 * 10) % 11
digito_1 = primeiro_numero if primeiro_numero <= 9 else 0


numeros_2 = []
for i in range(10):
    d = int(cpf_conta[i])
    numeros_2.append(d)

multiplicar_2 = 11
soma_numeros_2 = 0

for numero in numeros_2:
    soma_numeros_2 += numero * multiplicar_2
    multiplicar_2 -= 1

segundo_numero = (soma_numeros_2 * 10) % 11
digito_2 = segundo_numero if segundo_numero <= 9 else 0

dois_ultimos = int(str(digito_1) + str(digito_2))

if dois_ultimos == int(cpf_conta[-2::1]):
    print(f"O {cpf} é valido")
else:
    print("CPF invalido")