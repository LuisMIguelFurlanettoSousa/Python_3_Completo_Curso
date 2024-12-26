# Exercício - sistema de perguntas e respostas


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

for i in range(0, len(perguntas)):
    resp = ''
    print(perguntas[i]["Pergunta"], end="\n\n")

    print("Opções: ")
    for i, v in enumerate(perguntas[i]["Opções"]):
        print(f"{i}) {v}")

    resp = input("Escolha uma opçao: ")

    if resp == perguntas[i]["Opções"].index(perguntas[i]["Opções"]):
        resp_acertadas += 1

print(f"Voçê acertou {resp_acertadas} respostas")