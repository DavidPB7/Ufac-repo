import tkinter as tk

janela = tk.Tk()

janela.title('Pack')

lbl1 = tk.Label(janela, text='LEFT', bg='red')
lbl1.pack(padx=20, ipadx=20, side=tk.LEFT)

lbl2 = tk.Label(janela, text='RIGHT', bg='blue')
lbl2.pack(side=tk.RIGHT, fill=tk.Y)

janela.mainloop()
