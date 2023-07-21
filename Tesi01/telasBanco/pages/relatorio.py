import tkinter as tk
from tkinter import ttk


class Relatorio():
    def __init__(self, master):
        self.janela = master
        colunas = ('nome', 'operacao', 'valor')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, height=5, show='headings')
        self.tvw.grid()

        #Cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('operacao', text='Operação')
        self.tvw.heading('valor', text='Valor')

        #Colunas
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('operacao', minwidth=100, width=100)
        self.tvw.column('valor', minwidth=300, width=300)

        #Linhas
        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac'])
        self.tvw.insert('', 'end', values=['Fulano', '99999', 'fulano@ufac'])
        self.tvw.insert('', 'end', values=['Beltrano', '99999', 'beltrano@ufac'])
        self.tvw.insert('', 'end', values=['Ciclano', '99999', 'ciclano@ufac'])
        self.tvw.insert('', 'end', values=['Pek', '99999', 'pek@ufac'])
        self.tvw.insert('', 'end', values=['Segovinha', '99999', 'pek@ufac'])
        self.tvw.insert('', 'end', values=['Orelhano', '99999', 'pek@ufac'])
        self.tvw.insert('', 'end', values=['Pedro Raul', '99999', 'pek@ufac'])

        #Barra de rolagem
        scb = tk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.tvw.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.tvw.config(yscrollcommand=scb.set)

    def cadastrar(self):
        self.top_cadastrar = tk.Toplevel()
        lbl_nome = tk.Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=1)
        lbl_telefone = tk.Label()
        lbl_telefone.grid


app = tk.Tk()
Relatorio(app)
app.mainloop()