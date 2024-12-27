perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

resp_acertadas = 0

for pergunta in perguntas:
    print(pergunta["Pergunta"], end="\n\n")

    print("Opções: ")
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f"{i}) {opcao}")

    resp = input("Escolha uma opção (digite o número): ")

    if resp.isdigit():
        resp_int = int(resp)
        if resp_int >= 0 and resp_int <= len(pergunta['Opções']):

            if pergunta["Opções"][resp_int] == pergunta["Resposta"]:
                print("Resposta correta!\n")
                resp_acertadas += 1
            else:
                print("resposta errada!")
        else:
            print(f"Erro: {IndexError.__name__} detectado, Resposta errada!\n")
    else:
        print(f"Erro: {ValueError.__name__} detectado, Informe apenas numeros!!")

print(f"Você acertou {resp_acertadas} respostas.")
