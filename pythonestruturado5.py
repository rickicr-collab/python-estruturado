def somar_pares(lista): # definir função somar_pares com paramentro em lista
    soma = 0 # atribuir um valor inicial a soma como zero
    for elem in lista: # laço de repetição for informando os elementos numa lista
        if elem % 2 == 0: # condiçional if com elementos sendo numeros pares 
            soma += elem # realizando a soma e contando a quantidade de numeros dentro do laço for 
    return soma # realizando o retorno de soma 
lista_teste = [2, 10, 3, 5, 6, 7, 1] # criando uma lista qualquer para teste
pares = somar_pares(lista_teste) # criando a variavel pares ligando a função pre criada somar_pares com o parametro (lista _teste)
print('A soma dos elementos pares é {}'.format(pares))