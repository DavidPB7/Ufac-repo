import tkinter as tk


class Tela:
    def mostrar(self):
        lbl_mostrar = tk.Label(self.janela)
        lbl_mostrar2 = tk.Label(self.janela)
        lbl_mostrar['text'] = self.basico.get()
        lbl_mostrar2['text'] = self.avancado.get()
        lbl_mostrar.pack()
        lbl_mostrar2.pack()

    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')
        self.basico = tk.IntVar()
        self.avancado = tk.IntVar()

        cbt_basico = tk.Checkbutton(self.janela, text='Básico', variable=self.basico, command=self.mostrar)
        cbt_basico.pack()
        cbt_avancado = tk.Checkbutton(self.janela, text='Avançado', variable=self.avancado, command=self.mostrar)
        cbt_avancado.pack()

master = tk.Tk()
app = Tela(master)
master.mainloop()