import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("250x400")
janela.minsize(250, 400)
janela.maxsize(250, 400)

container1 = tk.Frame(janela, width=500, height=500, borderwidth=2, bg='gray')
container1.pack(expand=True)

#container2 = tk.Frame(janela, width=500, height=500, borderwidth=2, bg='red')
#container2.pack()

lbl_bloco1 = tk.Button(container1, text=' 7 ', bg='gray')
lbl_bloco1.grid(row=0, column=0, ipadx=3, ipady=2)

lbl_bloco2 = tk.Button(container1, text=' 8 ', bg='gray')
lbl_bloco2.grid(row=0, column=1, ipadx=3, ipady=2)

lbl_bloco3 = tk.Button(container1, text=' 9 ', bg='gray')
lbl_bloco3.grid(row=0, column=2, ipadx=3, ipady=2)

lbl_bloco4 = tk.Button(container1, text=' + ', bg='gray')
lbl_bloco4.grid(row=0, column=3, ipadx=3, ipady=2)

#--------------

lbl_bloco5 = tk.Button(container1, text=' 4 ', bg='gray')
lbl_bloco5.grid(row=1, column=0, ipadx=3, sticky="nsew", ipady=2)

lbl_bloco6 = tk.Button(container1, text=' 5 ', bg='gray')
lbl_bloco6.grid(row=1, column=1, ipadx=3, sticky="nsew", ipady=2)

lbl_bloco7 = tk.Button(container1, text=' 6 ', bg='gray')
lbl_bloco7.grid(row=1, column=2, ipadx=3, sticky="nsew", ipady=2)

lbl_bloco8 = tk.Button(container1, text=' - ', bg='gray')
lbl_bloco8.grid(row=1, column=3, ipadx=3, sticky="nsew", ipady=2)

#--------------

lbl_bloco9 = tk.Button(container1, text=' 1 ', bg='gray')
lbl_bloco9.grid(row=2, column=0, ipadx=3, sticky="nsew", ipady=2)

lbl_bloco10 = tk.Button(container1, text=' 2 ', bg='gray')
lbl_bloco10.grid(row=2, column=1, sticky="nsew", ipady=2)

lbl_bloco11 = tk.Button(container1, text=' 3 ', bg='gray')
lbl_bloco11.grid(row=2, column=2, sticky="nsew", ipady=2)

lbl_bloco12 = tk.Button(container1, text=' * ', bg='gray')
lbl_bloco12.grid(row=2, column=3, sticky="nsew", ipady=2)

#--------------

lbl_bloco13 = tk.Button(container1, text=' 0 ', bg='gray')
lbl_bloco13.grid(row=3, column=0, sticky="nsew", ipady=2)

lbl_bloco14 = tk.Button(container1, text=' . ', bg='gray')
lbl_bloco14.grid(row=3, column=1, sticky="nsew", ipady=2)

lbl_bloco15 = tk.Button(container1, text=' C ', bg='gray')
lbl_bloco15.grid(row=3, column=2, sticky="nsew", ipady=2)

lbl_bloco16 = tk.Button(container1, text=' / ', bg='gray')
lbl_bloco16.grid(row=3, column=3, sticky="nsew", ipady=2)

lbl_bloco17 = tk.Button(container1, text=' = ', bg='green')
lbl_bloco17.grid(row=4, column=0, columnspan=4, sticky='ew')

janela.mainloop()
