"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

passou_do_radar = (local_carro >= (LOCAL_1 - RADAR_RANGE)) and (local_carro <= (LOCAL_1 + RADAR_RANGE))

levou_multa = passou_do_radar and (velocidade > RADAR_1)


if passou_do_radar:
    print("O carro passou do radar")

if levou_multa:
    print("levou multa")


