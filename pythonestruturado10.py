#exercicio tratando excecoes de valores 
#------exercicio 01--------------#
while True:
    try: #função de tratamento de exceção
        x = int(input('Digite um numero:')) # valor a ser inserido pelo usuario no terminal declarada com classe primitiva inteira
        break # ao realizar a condição especificada no try para exceção para o laço while e fecha o programa 
    except ValueError: # condição para tratar a exceção delcarada
        print('Insira um valor valido! ') # informação a ser inserida na condição da exceçao 
print('Fim')