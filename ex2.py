def fibonacciLista(target):
    listaFibonacci = [1,1]
    while target > listaFibonacci[-1]:
        listaFibonacci.append(listaFibonacci[-1] + listaFibonacci[-2])
        if target < listaFibonacci[-1]:
            return 'Número não está na sequência de Fibonacci'
        elif target == listaFibonacci[-1]:
            return 'Número está na sequência de Fibonacci'
        
target = int(input('Insira um numero: '))

print(fibonacciLista(target))