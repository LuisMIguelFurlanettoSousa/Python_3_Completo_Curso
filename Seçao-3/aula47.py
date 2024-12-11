"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = "abobora".lower()
palavra_escondida = "*" * len(palavra_secreta)
cont = 0

while True:
    letra = input("Digite uma letra: ").lower()
    cont += 1

    if len(letra) > 1:
        print("Digite apenas uma letra!")
        continue

    if not letra:
        continue

    nova_palavra = ""
    for l in range(len(palavra_secreta)):
        if letra == palavra_secreta[l]:
            nova_palavra += letra
        else:
            nova_palavra += palavra_escondida[l]
        
    palavra_escondida = nova_palavra

    print(palavra_escondida)

    if palavra_escondida == palavra_secreta:
        print(
            "VC GANHOU PARABENS!!!\n"
            f"A palavra secreta era: {palavra_secreta}"
            )
        