import tkinter as tk


class Tela:

    def verificar(self):
        lbl_verifica = tk.Label(self.janela, text='Parabéns, você conseguiu passar!2!')
        lbl_verifica.pack()

    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')

        # tamanho maximo:
        self.janela.maxsize(800, 600)
        lbl_usuario = tk.Label(self.janela, text='Usuário')
        lbl_usuario.pack()

        ent_usuario = tk.Entry(self.janela, width=30)
        ent_usuario.pack()

        lbl_senha = tk.Label(self.janela, text='Senha')
        lbl_senha.pack()

        ent_senha = tk.Entry(self.janela, width=30, show='*')
        ent_senha.pack()

        btn_verificar = tk.Button(self.janela, text='Logar', command=self.verificar)
        btn_verificar.pack()

        btn_fechar = tk.Button(self.janela, text='Fechar', command=self.janela.destroy)
        btn_fechar.pack()


master = tk.Tk()
app = Tela(master)
master.mainloop()