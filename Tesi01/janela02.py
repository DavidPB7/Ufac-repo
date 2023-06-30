import tkinter as tk

janela = tk.Tk()


janela.mainloop()

import tkinter as tk

class Tela:
    def mostrar(self):
        lbl_mostrar = tk.Label(self.janela, text=self.v.get())
        lbl_mostrar.pack()

    def __init__(self, master): #customizar a janela
        
        self.janela = master
        self.janela.title("Soma Simples")
        self.janela.geometry("200x200")
        self.janela.minsize(200, 200)
        self.janela.maxsize(200, 200)
        self.v = tk.StringVar()
        self.v.set('bd1')

        lbl_user = tk.Label(janela, text='Número1:')
        lbl_user.grid(row=0, column=0)

        lbl_pass = tk.Label(janela, text='Número2:')
        lbl_pass.grid(row=1, column=0)

        ent_user = tk.Entry(janela)
        ent_user.grid(row=0, column=1)

        ent_pass = tk.Entry(janela)
        ent_pass.grid(row=1, column=1)

        btn = tk.Button(janela, text='Somar')
        btn.grid(row=2, column=0, columnspan=2)


        # self.janela.title('Exemplo RadioButton')
        # self.janela.geometry('400x400')
        # self.v = tk.StringVar()
        # self.v.set('bd1')
        # lbl_escolha = tk.Label(self.janela, text='Escolha uma Disciplina:')
        # lbl_escolha.pack()
        # rbt_lp1 = tk.Radiobutton(self.janela, text='LP1', value='lp1', variable=self.v, selectcolor='grey', command=self.mostrar)
        # rbt_lp1.pack()
        # rbt_tesi1 = tk.Radiobutton(self.janela, text='TESI 1', value='tesi1', variable=self.v, selectcolor='grey', command=self.mostrar)
        # rbt_tesi1.pack()
        # rbt_bd1 = tk.Radiobutton(self.janela, text='BD 1', value='bd1', variable=self.v, selectcolor='grey', command=self.mostrar)
        # rbt_bd1.pack()

app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()
