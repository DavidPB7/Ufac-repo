import tkinter as tk

class Tela:

    def mostrar(self):
        if self.v.get() == 1:
            self.cbt1.config(state=tk.ACTIVE)
        else:
            self.cbt1.config(state=tk.DISABLED)

    def __init__(self, master):
        self.janela = master
        self.janela.title('Atividade01')
        self.janela.geometry('400x500')
        self.v = tk.IntVar(self.janela, 0)


        rbt2 = tk.Radiobutton(self.janela, text='Sim', value=1, variable=self.v, command=self.mostrar)
        rbt2.pack()
        rbt2 = tk.Radiobutton(self.janela, text='Não', value=0, variable=self.v, command=self.mostrar)
        rbt2.pack()


        self.cbt1 = tk.Checkbutton(self.janela, text='Flamengo', state=tk.DISABLED)
        self.cbt1.pack()

        cbt2 = tk.Checkbutton(self.janela, text='Vasco', state=tk.DISABLED)
        cbt2.pack()

        cbt3 = tk.Checkbutton(self.janela, text='Bahia', state=tk.DISABLED)
        cbt3.pack()

        cbt4 = tk.Checkbutton(self.janela, text='Botafogo', state=tk.DISABLED)
        cbt4.pack()



master = tk.Tk()
app = Tela(master)
master.mainloop()
