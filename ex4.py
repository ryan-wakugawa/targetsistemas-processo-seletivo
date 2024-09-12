faturamentoEstados =  {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'OUTROS': 19849.53 
}

def calcularPorcentagem(json: dict):
    total = (sum(json.values()))
    for estado in json:
        json[estado] = json[estado] * 100 / total
    return json

def printFaturamento(json: dict):
    for estado in json:
        print(f'{estado}: {json[estado]:.2f}%')

faturamentoEstadosPorcentagem = calcularPorcentagem(faturamentoEstados)
printFaturamento(faturamentoEstadosPorcentagem)
