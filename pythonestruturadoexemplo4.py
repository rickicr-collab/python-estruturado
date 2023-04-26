# ------Interfaçe grafica-----------#
# primeiras interações com interfaçe grafica trabalhando com bliblioteca tkinter
from tkinter import *

def funcClicar():
    print('Botão pressionado')

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = 'Minha Janela exibida')
texto.pack()

pic = PhotoImage(file = 'images.png')
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()