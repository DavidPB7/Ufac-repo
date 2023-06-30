import tkinter as tk
janela = tk.Tk()
janela.title('Primeira Janela')

#tamanho inicial:
janela.geometry('500x500')

# #tamanho maximo:
# janela.maxsize(800, 600)
# ------------------------
# #tamanho minimo:
# janela.minsize(200, 400)

#impede o usuario de redimensionar a tela
janela.resizable(width=False, height=False)

container1 = tk.Frame(janela, width=200, height=200, bg='#FF6347', borderwidth=10, relief=tk.RAISED)
container1.pack()

container2 = tk.Frame(janela, width=100, height=100, bg='#1C1C1C', borderwidth=5, relief=tk.SUNKEN)
container2.pack()


janela.mainloop()