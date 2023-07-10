import tkinter as tk



def limpa_tela(self):
    self.lbl.config(text='')
 
def clicou1(event):
    if event.char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        resultado = f"Tecla Normal: {event.char}"
    
    elif event.keysym in ["Control_L", "Control_R", "Shift_L", "Shift_R", "Tab", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]:
        resultado = f"Tecla Especial: {event.keysym}"
    
    else:
        resultado = f"Tecla de Pontuação: {event.keysym}"
    
    lbl = tk.Label(master, text=resultado)
    lbl.pack()


class Tela:
    def __init__(self, master):
            self.janela = master
            self.janela.title('Terceira Janela')
            self.janela.geometry('300x500')

            master.bind("<KeyPress>", clicou1)

            self.btn1 = tk.Button(self.janela, text='Pressione qualquer tecla')
            self.btn1.pack()

            self.btn2 = tk.Button(self.janela, text='Limpar Tela', command=limpa_tela)
            self.btn2.pack(side='bottom')



master = tk.Tk()
app = Tela(master)
master.mainloop()

