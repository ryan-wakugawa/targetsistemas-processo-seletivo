saida = []

entrada = input('Insira uma palavra/frase: ')

for i in range(len(entrada)-1, -1, -1):
    print(i)
    saida.append(entrada[i])
print(''.join(saida))