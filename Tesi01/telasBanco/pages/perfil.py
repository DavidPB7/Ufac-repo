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

        self.lbl_four = tk.Button(self.lbl_frm_one, text='Detalhes da conta', command=self.detalhes)
        self.lbl_four.grid(row=2, column=0, columnspan=2)

        # Label Frame 02

        self.lbl_frm_three = tk.LabelFrame(self.janela, text='Funcionalidades', font=('Tahoma', 12), height=100, width=100, border=0)
        self.lbl_frm_three.pack(anchor=tk.CENTER, pady=10)

        self.lbl_one = tk.Button(self.lbl_frm_three, text='Transferir', borderwidth=2, relief='groove', pady=15, padx=15, command=self.telaTransfere)
        self.lbl_one.grid(row=0, column=0)

        self.lbl_two = tk.Button(self.lbl_frm_three, text='Sacar', borderwidth=2, relief='groove', pady=15, padx=15, command=self.telaSaca)
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


    def telaSaca(self):
        self.janela_principal = self.janela  # Salvar a referência à janela principal

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

        self.frm_label1 = tk.LabelFrame(self.janela_saca, text='Area de Saque')
        self.frm_label1.pack()

        self.lbl01 = tk.Label(self.frm_label1, text="Qual é o valor do Saque?")
        self.lbl01.pack()

        self.lbl02 = tk.Label(self.frm_label1, text="Saldo disponível em conta para sacar: R$40,44")
        self.lbl02.pack()

        self.lbl03 = tk.Entry(self.frm_label1)
        self.lbl03.insert(tk.END, "R$0,00")
        self.lbl03.pack(pady=15, padx=10)

        self.lbl04 = tk.Button(self.frm_label1, text="Sacar", width=7, height=1, font=4, bg="#50fa7d", activebackground = '#0afa49')
        self.lbl04.pack(pady=5)

        

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

        self.frm_label2 = tk.LabelFrame(self.janela_transfere, text='Area pix')
        self.frm_label2.pack()

        self.lbl01 = tk.Label(self.frm_label2, text="Qual é o valor da transferência?")
        self.lbl01.pack()

        self.lbl02 = tk.Label(self.frm_label2, text="Saldo didponível em conta: R$40,44")
        self.lbl02.pack()

        self.lbl03 = tk.Entry(self.frm_label2)
        self.lbl03.insert(tk.END, "R$0,00")
        self.lbl03.pack(pady=15, padx=10)

        self.lbl04 = tk.Button(self.frm_label2, text="Confirmar", width=7, height=1, font=4, bg="#50fa7d", activebackground = '#0afa49')
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
