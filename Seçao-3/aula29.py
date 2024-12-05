"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input(
    "Vou dobrar o numero que vc digitar: "
    )

try: 
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)

    print(f"O dobro do {numero_str} é {numero_float * 2:.2f}")
except:
    print("isso nao é um numero")