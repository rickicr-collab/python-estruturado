#exercicio 03 --------------------------------------
nota1 = float(input('Digite primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media >= 7.0: # sinais de maior ou igual tem que seguir essa regra onde o maior fica antes do igua
  print(' a media do aluno é {:.2f} O aluno está aprovado parabens !!!'.format(media))
elif media >= 5.0:
  print('A media do aluno é {:.2f} o aluno está em recuperação!!!'.format(media))
else :
  media <= 5.0
  print('A media do aluno é {:.2f} o aluno está reprovado!!!'.format(media))