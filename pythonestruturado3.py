#exercicio 03 ---------------------------------------
quantidade = int(input('Qual a quantidade? '))
preço = 10 * quantidade
desconto1 = preço - (preço * 10 / 100)
desconto2 = preço - (preço * 20 / 100)
if quantidade <= 10:
  print('Esse é o preço normal sem desconto que fica R${} '.format(preço))
elif quantidade > 10 and quantidade <= 20:
  print('O preço fica R${} com desconto de 10%'.format(desconto1))
elif quantidade > 20:
  print('o preço  fica R${} com desconto de 20%'.format(desconto2))