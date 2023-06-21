import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Exemplo Text com Scrollbar')
        self.janela.geometry('400x400')
        #self.janela.maxsize(400)
        #self.janela.resizable(width=True,height=True)
        #Menu
        mnu_barra = tk.Menu(self.janela)
        mnu_arquivo = tk.Menu(mnu_barra, tearoff=0)
        mnu_barra.add_cascade(label='Arquivo', menu=mnu_arquivo)
        mnu_arquivo.add_command(label='Novo Arquivo...')
        mnu_arquivo.add_command(label='Sair', command=self.janela.destroy)
        self.janela.config(menu=mnu_barra)
        #Barra de rolagem
        scb_texto = tk.Scrollbar(self.janela)
        scb_texto.pack(side=tk.RIGHT, fill=tk.Y)
        #Caixa de Texto
        txt_obs = tk.Text(self.janela, height=5, width=50, yscrollcommand=scb_texto.set)
        txt_obs.pack(side=tk.LEFT, fill=tk.X)
        scb_texto.config(command=txt_obs.yview)
        #Caixa de texto com a barra automática
        txt_auto = ScrolledText(self.janela, width=50, height=5)
        txt_auto.pack()


app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()