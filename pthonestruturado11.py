def dividir (x, y):
    try:
        x = int(input('digite um valor:'))
        y = int(input('digite um valor:'))
        resultado = x / y
        print('A resposta é :', resultado)
    except ZeroDivisionError:
        print('Divisão por zero!!!')
x = 0
y = 0
dividir(x, y)