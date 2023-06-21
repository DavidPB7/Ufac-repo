import tkinter as tk

janela = tk.Tk()
janela.geometry('300x300')

lbl1 = tk.Label(janela, text='X=0, Y=0', bg='red')
lbl1.place(x=0, y=0, anchor=tk.CENTER)

lbl2 = tk.Label(janela, text='X=50, Y=99', bg='blue')
lbl2.place(relx=.5, rely=.5, anchor=tk.CENTER)

lbl3 = tk.Label(janela, text='X=100, Y=25', bg='yellow')
lbl3.place(x=100, y=25)

lbl4 = tk.Label(janela, text='X=5, Y=120', bg='green')
lbl4.place(x=5, y=120)




janela = tk.Tk()
janela.mainloop()