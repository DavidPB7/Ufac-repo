import tkinter as tk
from tkinter import ttk
from perfil import Perfil 

class Relatorio:
    def __init__(self, master):
        self.janela = master
        colunas = ('nome', 'operacao', 'valor', 'tipo')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, height=5, show='headings')
        self.tvw.grid()

        # Crie a instância da classe Perfil dentro do método __init__ da classe Relatorio
        self.perfil_instancia = Perfil()

        valor_do_perfil = self.perfil_instancia.validate_valor
        tipo_conta_perfil = self.perfil_instancia.validate_tipo
        #Cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('operacao', text='Operação')
        self.tvw.heading('valor', text='Valor')
        self.tvw.heading('tipo', text='Tipo de Conta')

        #Colunas
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('operacao', minwidth=100, width=100)
        self.tvw.column('valor', minwidth=300, width=300)
        self.tvw.column('tipo', minwidth=300, width=300)

        #Linhas
        self.tvw.insert('', 'end', values=['Carlin', valor_do_perfil, 'carlir@gmail.com', tipo_conta_perfil])
        self.tvw.insert('', 'end', values=['Carlin', valor_do_perfil, 'carlir@gmail.com', tipo_conta_perfil])
        self.tvw.insert('', 'end', values=['Carlin', valor_do_perfil, 'carlir@gmail.com', tipo_conta_perfil])
       

        #Barra de rolagem
        scb = tk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.tvw.yview)
        scb.grid(row=0, column=1, sticky='ns')
        self.tvw.config(yscrollcommand=scb.set)

    # def cadastrar(self):
    #     self.top_cadastrar = tk.Toplevel()
    #     lbl_nome = tk.Label(self.top_cadastrar, text='Nome:')
    #     lbl_nome.grid(row=1)
    #     lbl_telefone = tk.Label()
    #     lbl_telefone.grid

