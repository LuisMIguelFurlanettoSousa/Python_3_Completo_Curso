# exemplo de uso de sets

letras = set()
while True:
    letra = input("digite: ")
    letras.add(letra.lower())

    if "l" in letras:
        print("parabens vc achou a letra muito misteriosa sensacional em mds")
        break

    print(letras)