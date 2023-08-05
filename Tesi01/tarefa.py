import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#janela = tk.Tk()
janela = ttk.Window(themename='superhero')
lbl1 = tk.Label(janela, text='superhero', font=('Tahoma', 20))
lbl1.pack()

frm = ttk.LabelFrame(janela, text='Alguns widgets do tkinter')
frm.pack()

lbl2 = tk.Label(frm, text='Widget Label')
lbl2.pack()

frm1 = tk.Frame(frm)
frm1.pack()

label1 = tk.Entry(frm1, width=10)
label2 = tk.Label(frm1, text="Label 2")
label3 = tk.Button(frm1, text="Label 3")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)


janela.mainloop()
