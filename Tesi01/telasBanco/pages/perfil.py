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
        self.lbl_frm_one = tk.LabelFrame(self.janela, text='Minha Conta: ', font=('Tahoma', 12), height=100, width=100)
        self.lbl_frm_one.pack(anchor=tk.CENTER, pady=10)

        self.lbl_one = tk.Label(self.lbl_frm_one, text='Foto', borderwidth=4, relief='groove', pady=30, padx=30)
        self.lbl_one.grid(row=0, column=0)

        self.lbl_two = tk.Label(self.lbl_frm_one)
        self.lbl_two.grid(row=1, column=0)

        self.lbl_three = tk.Label(self.lbl_frm_one, text='Olá, Carlos!', pady=10)
        self.lbl_three.grid(row=0, column=1)

        self.four_pass = tk.Label(self.lbl_frm_one)
        self.four_pass.grid(row=1, column=1)

        self.lbl_four = tk.Button(self.lbl_frm_one, text='Detalhes da conta', command=self.detalhes)
        self.lbl_four.grid(row=2, column=0, columnspan=2)

        # Label Frame 02

        self.lbl_frm_three = tk.LabelFrame(self.janela, text='Funcionalidades: ', font=('Tahoma', 12), height=100, width=100, border=0)
        self.lbl_frm_three.pack(anchor=tk.CENTER, pady=10)

        self.lbl_one = tk.Button(self.lbl_frm_three, text='Transferir', borderwidth=2, relief='groove', pady=15, padx=15, command=self.telaTransfere)
        self.lbl_one.grid(row=0, column=0)

        self.lbl_two = tk.Button(self.lbl_frm_three, text='Sacar', borderwidth=2, relief='groove', pady=15, padx=15, command=self.telaSaca)
        self.lbl_two.grid(row=0, column=1)

        self.lbl_three = tk.Button(self.lbl_frm_three, text='Depositar', borderwidth=2, relief='groove', pady=15, padx=15, command=self.telaDeposito)
        self.lbl_three.grid(row=0, column=2)

        self.four_pass = tk.Button(self.lbl_frm_three, text='Relatórios', borderwidth=2, relief='groove', pady=15, padx=15)
        self.four_pass.grid(row=0, column=3)
        #
        # self.lbl_four = tk.Button(self.lbl_frm_three, text='Detalhes da conta')
        # self.lbl_four.grid(row=2, column=0, columnspan=2)


    # Tela detalhes da conta
    def detalhes(self):
        self.janela_detalhes = self.janela

        self.janela.withdraw()
        self.janela_detalhes = tk.Toplevel()

        self.janela_detalhes.title("Detalhes")
        self.janela_detalhes("400x400")

        def voltar():
            self.janela_detalhes.destroy()
            self.janela_principal.deiconify()  # Restaurar a janela principal

        btn_voltar = tk.Button(self.janela_detalhes, text="Voltar", borderwidth=1, relief='ridge', command=voltar)
        btn_voltar.pack(anchor="nw", pady=5, padx=5)

    #  Tela para sacar
    def telaSaca(self):
        self.janela_principal = self.janela  # Salvar a referência à janela principal

        #Variaveis do Entry para validação
        self.validate_valor = tk.StringVar()
        self.validate_valor.set(' ')

        self.janela.withdraw()
        self.janela_saca = tk.Toplevel()

        # Configurações da nova janela
        self.janela_saca.title("Saque")
        self.janela_saca.geometry("400x400")

        def voltar():
            self.janela_saca.destroy()
            self.janela_principal.deiconify()  # Restaurar a janela principal

        btn_voltar = tk.Button(self.janela_saca, text="Voltar", borderwidth=1, relief='ridge', command=voltar)
        btn_voltar.pack(anchor="nw", pady=5, padx=5)

        self.frm_label1 = tk.LabelFrame(self.janela_saca, text='Area de Saque', font=('Tahoma', 12))
        self.frm_label1.pack()

        self.lbl01 = tk.Label(self.frm_label1, text="Qual é o valor do Saque?")
        self.lbl01.pack()

        self.lbl02 = tk.Label(self.frm_label1, text="Saldo disponível em conta para sacar: R$40,44")
        self.lbl02.pack()

        self.lbl03 = tk.Entry(self.frm_label1, textvariable=self.validate_valor)
        self.lbl03.insert(tk.END, "R$0,00")
        self.lbl03.pack(pady=15, padx=10)

        self.rbt1 = tk.Radiobutton(self.frm_label1, text='Conta Poupança', value='pp')
        self.rbt1.pack()
        self.rbt2 = tk.Radiobutton(self.frm_label1, text='Conta Corrente', value='pc')
        self.rbt2.pack()

        # def confirmar():
        #     valor = self.validate_valor

        #     if (valor == '') or (valor == 0):
        #         messagebox.showinfo('Aviso', 'Valor está incorreto! Tente novamente!')
        #     else:
        #         self.janela.withdraw()
        #         self.home_page()

        self.lbl04 = tk.Button(self.frm_label1, text="Sacar", width=7, height=1, font=4, bg="#50fa7d", activebackground = '#0afa49', command=confirmar)
        self.lbl04.pack(pady=5)

        
    # Tela para transfência
    def telaTransfere(self):
        self.janela_principal = self.janela  # Salvar a referência à janela principal

        self.janela.withdraw()
        self.janela_transfere = tk.Toplevel()

        # Configurações da nova janela
        self.janela_transfere.title("Transferência")
        self.janela_transfere.geometry("400x400")

        def voltar():
            self.janela_transfere.destroy()
            self.janela_principal.deiconify()  # Restaurar a janela principal

        btn_voltar = tk.Button(self.janela_transfere, text="Voltar", borderwidth=1, relief='ridge', command=voltar)
        btn_voltar.pack(anchor="nw", pady=5, padx=5)

        self.frm_label2 = tk.LabelFrame(self.janela_transfere, text='Area pix', font=('Tahoma', 12))
        self.frm_label2.pack()

        self.lbl01 = tk.Label(self.frm_label2, text="Qual é o valor da transferência?")
        self.lbl01.pack()

        self.lbl02 = tk.Label(self.frm_label2, text="Saldo disponível em conta: R$40,44")
        self.lbl02.pack()

        self.lbl03 = tk.Entry(self.frm_label2)
        self.lbl03.insert(tk.END, "R$0,00")
        self.lbl03.pack(pady=15, padx=10)

        self.rbt1 = tk.Radiobutton(self.frm_label2, text='Conta Poupança', value='pp')
        self.rbt1.pack()
        self.rbt2 = tk.Radiobutton(self.frm_label2, text='Conta Corrente', value='pc')
        self.rbt2.pack()

        self.lbl04 = tk.Button(self.frm_label2, text="Confirmar", width=7, height=1, font=4, bg="#50fa7d", activebackground = '#0afa49')
        self.lbl04.pack(pady=5)

    # Tela para Deposito
    def telaDeposito(self):
        self.janela_principal = self.janela  # Salvar a referência à janela principal

        self.janela.withdraw()
        self.janela_deposito = tk.Toplevel()

        # Configurações da nova janela
        self.janela_deposito.title("Transferência")
        self.janela_deposito.geometry("400x400")

        def voltar():
            self.janela_deposito.destroy()
            self.janela_principal.deiconify()  # Restaurar a janela principal

        btn_voltar = tk.Button(self.janela_deposito, text="Voltar", borderwidth=1, relief='ridge', command=voltar)
        btn_voltar.pack(anchor="nw", pady=5, padx=5)

        self.frm_label3 = tk.LabelFrame(self.janela_deposito, text='Area Deposito', font=('Tahoma', 12))
        self.frm_label3.pack()

        self.lbl01 = tk.Label(self.frm_label3, text="Qual é o valor da Deposito?")
        self.lbl01.pack()

        self.lbl02 = tk.Label(self.frm_label3, text="Saldo disponível em conta: R$40,44")
        self.lbl02.pack()

        self.lbl03 = tk.Entry(self.frm_label3)
        self.lbl03.insert(tk.END, "R$0,00")
        self.lbl03.pack(pady=15, padx=10)

        self.rbt1 = tk.Radiobutton(self.frm_label3, text='Conta Poupança', value='pp')
        self.rbt1.pack()
        self.rbt2 = tk.Radiobutton(self.frm_label3, text='Conta Corrente', value='pc')
        self.rbt2.pack()

        self.lbl04 = tk.Button(self.frm_label3, text="Confirmar", width=7, height=1, font=4, bg="#50fa7d", activebackground = '#0afa49')
        self.lbl04.pack(pady=5)

            
app = tk.Tk()
Tela(app)
app.mainloop()




#Apagar texto de um entry como um placeholder

# def on_entry_click(event):
#     if entry.get() == "Digite aqui":
#         entry.delete(0, tk.END)
#         entry.config(foreground='black')

# def on_focus_out(event):
#     if entry.get() == "":
#         entry.insert(0, "Digite aqui")
#         entry.config(foreground='gray')

# root = tk.Tk()

# entry = tk.Entry(root, width=30, foreground='gray')
# entry.insert(0, "Digite aqui")
# entry.bind('<FocusIn>', on_entry_click)
# entry.bind('<FocusOut>', on_focus_out)
# entry.pack()
