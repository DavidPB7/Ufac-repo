import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')

        

        master.bind("<KeyPress>", self.clicou1)

        self.btn1 = tk.Button(self.janela, text='Pressione qualquer tecla')
        self.btn1.pack()

        self.lbl = tk.Label(master)
        self.lbl.pack()

        self.btn2 = tk.Button(self.janela, text='Limpar Tela', command=self.limpa_tela)
        self.btn2.pack(side='bottom')

    def limpa_tela(self):
        self.lbl.config(text='')

    def clicou1(self, event):
        if event.char.isalpha():
            resultado = f"Tecla Normal: {event.char}"
        elif event.keysym in ["Control_L", "Control_R", "Shift_L", "Shift_R", "Tab", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]:
            resultado = f"Tecla Especial: {event.keysym}"
        else:
            resultado = f"Tecla de Pontuação: {event.keysym}"
        
        self.lbl = tk.Label(master, text=resultado)
        self.lbl.pack()


master = tk.Tk()
app = Tela(master)
master.mainloop()