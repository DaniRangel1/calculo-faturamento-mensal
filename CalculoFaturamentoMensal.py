import json


with open('dados.json', 'r') as f:
    dados = json.load(f)


menor_valor = float('inf')
maior_valor = 0
soma_valores = 0
dias_acima_media = 0


for d in dados:
    if d['valor'] > 0:

        if d['valor'] < menor_valor:
            menor_valor = d['valor']

        if d['valor'] > maior_valor:
            maior_valor = d['valor']

        soma_valores += d['valor']


media_mensal = soma_valores / len([d for d in dados if d['valor'] > 0])


for d in dados:
    if d['valor'] > media_mensal:
        dias_acima_media += 1


print(f"Menor valor de faturamento diário: {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")