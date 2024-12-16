"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
compras = []

while True:
    try:
        print("Selecione uma opção: ")
        opcao = input("[I]nserir [A]pagar [L]istar: ").upper()

        if opcao not in "IAL" or not opcao:
            os.system("cls")
            print("Insira uma opção valida: [I, A, L]")
        elif opcao == "I":
            valor = input("Valor: ")
            compras.append(valor)
            os.system("cls")
            continue
        elif opcao == "A":
            if len(compras) == 0:
                os.system("cls")
                print("Nenhum item foi adicionado ainda!")
            else:
                try:
                    item_apagar = int(input("Informe o indice que deseja apagar: "))
                    compras.pop(item_apagar)
                except ValueError:
                    print("Digite um numero inteiro")
                except IndexError:
                    print("indice nao existe")
                except Exception:
                    print("Erro disconhecido")
        elif opcao == "L":
            os.system("cls")
            if len(compras) == 0:
                print("Nada foi inserido")
                continue
            for i, v in enumerate(compras):
                print(i, v)
            

    except EOFError or KeyboardInterrupt:
        break              