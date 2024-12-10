"""
Iterando strings com while
"""
#       012345678910
nome = "Luis Miguel" #iteravem
nova_string = ''

tamanho_nome = len(nome)

i = 0 
while i < tamanho_nome:
    nova_string += f"*{nome[i]}"
    i += 1

print(nova_string)