import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')

        #tamanho maximo:
        self.janela.maxsize(800, 600)
        lbl_usuario = tk.Label(self.janela, text='Usuário')
        lbl_usuario.pack()

        ent_usuario = tk.Entry(self.janela, width=30)
        ent_usuario.pack()

        lbl_senha = tk.Label(self.janela, text='Senha')
        lbl_senha.pack()

        ent_senha = tk.Entry(self.janela, width=30)
        ent_senha.pack()

master = tk.Tk()
app = Tela(master)
master.mainloop()