import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')
        #tamanho maximo:
        self.janela.maxsize(800, 600)
        primeira_lbl = tk.Label(self.janela, text='Anuncie Aqui', width=10, height=10, bg='blue', fg='red', font=('Ubuntu'))
        segunda_lbl = tk.Label(self.janela, text='Anuncie Aqui', width=10, height=10, bg='red', fg='blue', font=('Ubuntu'))
        primeira_lbl.pack()
        segunda_lbl.pack()


master = tk.Tk()
app = Tela(master)
master.mainloop()