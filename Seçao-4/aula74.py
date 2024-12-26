"""
Closure e funçoes que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

s1 = falar_bom_dia("luis")
s2 = falar_boa_noite("luis")

print(s1)
print(s2)
