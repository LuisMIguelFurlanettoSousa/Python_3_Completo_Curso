"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#Solução
# num = input("Digite um numero inteiro: ")

# try:
#     num_inteiro = int(num)

#     if num_inteiro % 2 == 0:
#         print("par")
#     else:
#         print("impar")
# except:
#     print("Numero invalido, digite um numero inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hr = input("Informe a hr certa: ")

# try:
#     hr_inteira = int(hr)

#     if 0 <= hr_inteira <= 11:
#         print("bom dia")
#     elif 12 <= hr_inteira <= 17:
#         print("boa tarde")
#     elif 18 <= hr_inteira <= 23:
#         print("boa noite")
#     else:
#         print("Nao conheço essa hr")

# except:
#     print("Hora invalida, informe um numero inteiro")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Insira o seu primeiro nome: ")

if " " not in nome:
    tamanho_nome = len(nome)
    tamanho5_6 = tamanho_nome == 5 or tamanho_nome == 6
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho5_6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Insira apenas o primeiro nome!")
