import matplotlib.pyplot as plt # bliblioteca para gerar graficos na tela 
import numpy as np # bliblioteca focada em trabalhar com entrada de dados 

np.random.seed(1) # função da bliblioteca numpy pra gerar randomização dos dados solicitados 
dados = np.random.normal(loc = 20, scale = 2,  size = 1000) # requisitos e condições solicitadas para gerar o grafico em tela 
plt.hist(dados, color = 'yellow', ec = 'red') # formatação e customização das cores nos graficos 