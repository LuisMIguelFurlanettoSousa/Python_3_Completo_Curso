frase = "O Python é uma linguagem da programação"\
        "multiparadigrama."\
        "Python foi criador por Guido Van Rossum.".lower()

i = 0
maior_qnt = 0
maior_letra = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue
    
    qnt_atual = frase.count(letra_atual)

    if qnt_atual > maior_qnt:
        maior_qnt = qnt_atual
        maior_letra = letra_atual
    
    i += 1


print(f"A letra que apareceu mais vezes foi '{maior_letra}' com {maior_qnt} apariçoes")


