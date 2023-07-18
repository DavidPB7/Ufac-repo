import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Tela:
    ####### PERFIL ########
    def __init__(self, master):
        self.janela = master
        self.janela.title('Banco Pague Mais Juros - PERFIL')
        self.janela.geometry('400x400')

        # Label Frame 01

        # Label Frame 01
        self.lbl_frm_one = tk.LabelFrame(self.janela, text='Minha Conta', font=('Tahoma', 12), height=100, width=100)
        self.lbl_frm_one.pack(anchor=tk.CENTER, pady=10)

        self.lbl_one = tk.Label(self.lbl_frm_one, text='Foto', borderwidth=4, relief='groove', pady=30, padx=30)
        self.lbl_one.grid(row=0, column=0)

        self.lbl_two = tk.Label(self.lbl_frm_one)
        self.lbl_two.grid(row=1, column=0)

        self.lbl_three = tk.Label(self.lbl_frm_one, text='Olá, Carlos!', pady=10)
        self.lbl_three.grid(row=0, column=1)

        self.four_pass = tk.Label(self.lbl_frm_one)
        self.four_pass.grid(row=1, column=1)

        self.lbl_four = tk.Button(self.lbl_frm_one, text='Detalhes da conta')
        self.lbl_four.grid(row=2, column=0, columnspan=2)

        # Label Frame 02

        self.lbl_frm_three = tk.LabelFrame(self.janela, text='Funcionalidades', font=('Tahoma', 12), height=100, width=100, border=0)
        self.lbl_frm_three.pack(anchor=tk.CENTER, pady=10)

        self.lbl_one = tk.Button(self.lbl_frm_three, text='Transferir', borderwidth=2, relief='groove', pady=15, padx=15, command="telaTransfere")
        self.lbl_one.grid(row=0, column=0)

        self.lbl_two = tk.Button(self.lbl_frm_three, text='Sacar', borderwidth=2, relief='groove', pady=15, padx=15)
        self.lbl_two.grid(row=0, column=1)

        self.lbl_three = tk.Button(self.lbl_frm_three, text='Depositar', borderwidth=2, relief='groove', pady=15, padx=15)
        self.lbl_three.grid(row=0, column=2)

        self.four_pass = tk.Button(self.lbl_frm_three, text='Investir', borderwidth=2, relief='groove', pady=15, padx=15)
        self.four_pass.grid(row=0, column=3)
        #
        # self.lbl_four = tk.Button(self.lbl_frm_three, text='Detalhes da conta')
        # self.lbl_four.grid(row=2, column=0, columnspan=2)

        # Label Frame 03
        self.lbl_frm_two = tk.LabelFrame(self.janela, font=('Tahoma', 12), height=100, width=100)
        self.lbl_frm_two.pack(anchor=tk.CENTER)

        self.btn_one = tk.Button(self.lbl_frm_two, text='Boleto', borderwidth=1, relief='ridge', pady=30, padx=30)
        self.btn_one.grid(row=0, column=0)

        self.btn_two = tk.Button(self.lbl_frm_two, text='Vantagens', borderwidth=1, relief='ridge', pady=30, padx=30)
        self.btn_two.grid(row=0, column=1)


    def telaTransfere():
        self.janela.withdraw()
        

app = tk.Tk()
Tela(app)
app.mainloop()
