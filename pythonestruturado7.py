#verificando se um numero é primo ou não
# --------estrategia 01 ---------------
def ehprimo(n):
    if n < 2:
        return False
    i = n // 2
    while i < 1:
        if n % i == 0:
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'o numero {numero} NÃO é Primo'
    if(resultado):
        mensagem = f'O numero {numero} É PRIMO'
    return mensagem

numero = 7
resultado = ehprimo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)