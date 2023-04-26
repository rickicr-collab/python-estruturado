#condições if ´else  
#exemplo usando as condições if, else e tambem elif caso necessario 
#-----estrategia 01---------------------------
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
maior = 0
if num1 > num2:
  maior = num1
  print('{} é o maior numero'.format(num1))
  print('{} é o menor numero'.format(num2))
else:
  maior = num2
  print('{} é o numero maior'.format(num2))
  print('{} é o numero menor'.format(num1))

#----- estrategia 02---------------------------
a = 10
b = 20
maior = a
if (b>maior):
  maior = b
  print(f'o maior numero é {maior}')