import json

listaFatura:list = json.load(open('dados.json'))
listaFatura.sort(key=lambda x: x['valor'])
listaFaturaFiltrada = []
soma = 0

for i in listaFatura:
    if i['valor'] > 0:
        listaFaturaFiltrada.append(i)
        
for i in listaFaturaFiltrada:
    soma = i['valor'] + soma
    
média:float = soma / len(listaFaturaFiltrada)

def countHigherThanAverage(lista:list):
    count = 0
    for i in lista:
        if i['valor'] > 0:
            print(i['valor'])
            count += 1
    return count

print("Menor valor de faturamento ocorrido em um dia do mês: ", str(listaFaturaFiltrada[0]['valor']), " no dia " , str(listaFaturaFiltrada[0]['dia']))
print("Maior valor de faturamento ocorrido em um dia do mês: ", str(listaFaturaFiltrada[-1]['valor']), " no dia " , str(listaFaturaFiltrada[-1]['dia']))
print('Média de faturamento mensal: ', média)
print("Dias com faturamento acima da média: ", countHigherThanAverage(listaFaturaFiltrada))