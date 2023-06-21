import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.janela.title('Primeira Janela')
        btn = tk.Button(self.janela, text='New Windon', command=self.nova_janela).pack()


    def nova_janela(self):
        self.toplevel = tk.Toplevel()
        self.toplevel.geometry('300x100')
        self.toplevel.title('top Level Janela')
        #self.janela.withdraw() #Oculta a janela principal
        self.toplevel.grab_set() #Fixar toplevel
        btn2 = tk.Button(self.toplevel, text='Back', command='voltar').pack()

    def voltar(self):
        self.janela.destroy()
        self.janela.deiconify()

app = tk.Tk()
master = Tela(app)
app.mainloop()