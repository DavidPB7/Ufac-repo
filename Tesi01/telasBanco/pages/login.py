import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from cliente import Cliente


# import classes.banco
# import classes.conta


class Tela:
    ####### LOGIN ########
    def __init__(self, master):
        self.janela = master
        self.janela.title('Banco Pague Mais Juros - LOGIN')

        self.cadastros = []
        self.cliente_logado = None
        # Label Frame
        self.lbl_frm_one = tk.LabelFrame(self.janela, text='LOGIN', font=('Tahoma', 20), pady=50, padx=50,
                                         labelanchor=tk.N)
        self.lbl_frm_one.pack(anchor=tk.CENTER)

        # Frame para colocar email e senha
        self.frm_one = tk.Label(self.lbl_frm_one)
        self.frm_one.pack()
        # Variaveis do Entry para validação
        self.validate_email = tk.StringVar()
        self.validate_email.set(' ')

        self.validate_senha = tk.StringVar()
        self.validate_senha.set('')

        # Label e Entry de email e senha
        self.lbl_email = tk.Label(self.frm_one, text='E-mail:', font=('Arial', 15))
        self.lbl_email.grid(row=0, column=0, pady=20)
        self.ent_email = tk.Entry(self.frm_one, width=30, font=('Arial', 15), textvariable=self.validate_email)
        self.ent_email.grid(row=0, column=1, pady=20)
        self.lbl_senha = tk.Label(self.frm_one, text='Senha:', font=('Arial', 15))
        self.lbl_senha.grid(row=1, column=0, pady=20)
        self.ent_senha = tk.Entry(self.frm_one, width=30, font=('Arial', 15), show='*',
                                  textvariable=self.validate_senha)
        self.ent_senha.grid(row=1, column=1, pady=20)

        # Frame para colocar os botões
        self.frm_two = tk.Frame(self.lbl_frm_one)
        self.frm_two.pack()
        # Botões
        self.btn_logar = tk.Button(self.frm_two, text='Entrar', width=10, height=1, font=10, bg="#50fa7d",
                                   activebackground='#0afa49', command=self.entrar)
        self.btn_logar.grid(row=0, column=0, padx=5, pady=10)
        self.btn_exit = tk.Button(self.frm_two, text='Sair', width=10, height=1, font=10, bg="#ff4f4f",
                                  activebackground='#fc0505', command=self.janela.destroy)
        self.btn_exit.grid(row=0, column=1, padx=5, pady=10)
        self.btn_register = tk.Button(self.frm_two, text='Cadastre-se', width=10, height=1, font=10, bg="#2798f5",
                                      activebackground='#0525f7', command=self.cadastro)
        self.btn_register.grid(row=0, column=2, padx=5, pady=10)

    def verificar_login(self, email, senha):
        for cliente in self.cadastros:
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return cliente
            elif cliente.get_email() == "admin@gmail.com" and cliente.get_senha() == senha == "123":
                return cliente
            else:
                return False
        return None

    def entrar(self):
        email = self.validate_email.get()
        senha = self.validate_senha.get()

        cliente_logado = self.verificar_login(email, senha)
        if cliente_logado:
            self.cliente_logado = cliente_logado
            self.janela.withdraw()
            self.home_page()
        else:
            messagebox.showinfo('Aviso', 'Email ou senha incorretos! Tente novamente!')

    def cadastro(self):
        self.janela.withdraw()

        self.toplevel = tk.Toplevel()
        self.toplevel.title('Banco Pague Mais Juros - CADASTRO')

        self.frm_label_register = tk.LabelFrame(self.toplevel, text='CADASTRO', font=('Tahoma', 20), pady=50, padx=50,
                                                labelanchor=tk.N)
        self.frm_label_register.pack()

        self.frm_dados = tk.Frame(self.frm_label_register)
        self.frm_dados.pack()
        self.frm_botoes = tk.Frame(self.frm_label_register)
        self.frm_botoes.pack()

        self.nome = tk.StringVar()
        self.nome.set(' ')
        self.senha = tk.StringVar()
        self.senha.set('')
        self.email = tk.StringVar()
        self.email.set(' ')

        self.lbl_nome = tk.Label(self.frm_dados, text='Name:', font=('Arial', 15))
        self.lbl_nome.grid(row=0, column=0, pady=20)
        self.ent_name = tk.Entry(self.frm_dados, width=30, font=('Arial', 15), textvariable=self.nome)
        self.ent_name.grid(row=0, column=1, pady=20)

        self.lbl_email = tk.Label(self.frm_dados, text='E-mail:', font=('Arial', 15))
        self.lbl_email.grid(row=1, column=0, pady=20)
        self.ent_email = tk.Entry(self.frm_dados, width=30, font=('Arial', 15), textvariable=self.email)
        self.ent_email.grid(row=1, column=1, pady=20)

        self.lbl_senha = tk.Label(self.frm_dados, text='Senha:', font=('Arial', 15))
        self.lbl_senha.grid(row=2, column=0, pady=20)
        self.ent_senha = tk.Entry(self.frm_dados, width=30, font=('Arial', 15), show='*', textvariable=self.senha)
        self.ent_senha.grid(row=2, column=1, pady=20)

        # Botões
        self.btn_salvar = tk.Button(self.frm_botoes, text='Salvar', width=10, height=1, font=10, bg="#50fa7d",
                                    activebackground='#0afa49', command=self.cadastrar)
        self.btn_salvar.grid(row=0, column=0, padx=5, pady=10)

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', width=10, height=1, font=10, bg="#2798f5",
                                    activebackground='#0525f7', command=self.voltar)
        self.btn_voltar.grid(row=0, column=1, padx=5, pady=10)

    def cadastrar(self):
        nome = self.nome.get()
        email = self.email.get()
        senha = self.senha.get()

        if (nome == ' ') or (email == ' ') or (senha == ''):
            messagebox.showinfo('Aviso', 'Preencha todos os campos!')
        else:
            self.toplevel.destroy()
            self.janela.deiconify()

    ####### LOGIN ########

    ####### HOME PAGE ########
    def home_page(self):
        self.top_home_page = tk.Toplevel(self.janela)
        self.top_home_page.title('Banco Pague Mais Juros')
        self.top_home_page.geometry('1280x960')
        self.top_home_page.config(bg='#f1dec3')

        mnu_barra = tk.Menu(self.top_home_page)  # Barra
        mnu_banco = tk.Menu(mnu_barra, tearoff=0)  # Item
        mnu_barra.add_cascade(label='Banco', menu=mnu_banco)
        mnu_banco.add_command(label='Clientes', command=self.tabela)  # Sub-Item
        mnu_banco.add_command(label='Contas', command=None)

        mnu_ajuda = tk.Menu(mnu_barra, tearoff=0)  # Adicionando o terceiro menu e comandos
        mnu_barra.add_cascade(label='Ajuda', menu=mnu_ajuda)
        mnu_ajuda.add_command(label='Sobre', command=None)
        mnu_ajuda.add_command(label='Dicas', command=None)
        mnu_ajuda.add_command(label='Como usar?', command=None)

        mnu_logout = tk.Menu(mnu_barra, tearoff=0)  # Adicionando o terceiro menu e comandos
        mnu_barra.add_cascade(label='Logout', menu=mnu_logout)
        mnu_logout.add_command(label='Sair', command=self.sair)

        self.top_home_page.config(menu=mnu_barra)

        # Criando Frames
        self.frame_nome = tk.Frame(self.top_home_page)
        self.frame_buttons = tk.Frame(self.top_home_page)
        self.frame_nome.pack()
        self.frame_buttons.pack()

        # Label
        self.lbl_nome_banco = tk.Label(self.frame_nome, text='BANCO PAGUE MAIS JUROS', bg='#f1dec3', font=100)
        self.lbl_nome_banco.pack(anchor=tk.CENTER)

        # Button 1(Banco)
        self.image_banco = tk.PhotoImage(file='pages/banco.png')
        self.image_banco_red = self.image_banco.subsample(4, 4)
        self.btn_banco = tk.Button(self.top_home_page, image=self.image_banco_red, text="Banco", compound='bottom',
                                   font=20, command=None)
        self.btn_banco.image = self.image_banco_red
        self.btn_banco.pack(side=tk.RIGHT, ancho=tk.CENTER, expand=True)
        # Button 2(Cadastro)
        self.image_cad = tk.PhotoImage(file='pages/cadastro.png')
        self.image_cad_red = self.image_cad.subsample(4, 4)
        self.btn_cad = tk.Button(self.top_home_page, image=self.image_cad_red, text="Cadastro", compound='bottom',
                                 font=20, command=self.cadastro_cliente)
        self.btn_cad.image = self.image_cad_red
        self.btn_cad.pack(side=tk.RIGHT, ancho=tk.CENTER, expand=True)
        # Button 3(Relatorio)
        self.image_relatorios = tk.PhotoImage(file='pages/relatorios.png')
        self.image_relatorios_red = self.image_relatorios.subsample(4, 4)
        self.btn_relatorios = tk.Button(self.top_home_page, image=self.image_relatorios_red, text="Relatório",
                                        compound='bottom', font=20, command=None)
        self.btn_relatorios.image = self.image_relatorios_red
        self.btn_relatorios.pack(side=tk.RIGHT, ancho=tk.CENTER, expand=True)

    def sair(self):
        self.top_home_page.destroy()
        self.janela.deiconify()

    def voltar(self):
        self.toplevel.destroy()
        self.janela.deiconify()

    ####### CADASTRO CLIENTES ########

    ####### CADASTRO CLIENTES ########
    def cadastro_cliente(self):
        self.top_home_page.destroy()

        self.top_cliente = tk.Toplevel(self.janela)

        self.frm_label_cli = tk.LabelFrame(self.top_cliente, text='CADASTRO CLIENTE', font=('Tahoma', 20), pady=50,
                                           padx=50, labelanchor=tk.N)
        self.frm_label_cli.pack()

        self.frm_dados_cli = tk.Frame(self.frm_label_cli)
        self.frm_dados_cli.pack()
        self.frm_botoes_cli = tk.Frame(self.frm_label_cli)
        self.frm_botoes_cli.pack()

        self.nome_cli = tk.StringVar()
        self.nome_cli.set('')
        self.cpf_cli = tk.StringVar()
        self.cpf_cli.set('')
        self.endereco_cli = tk.StringVar()
        self.endereco_cli.set('')

        self.lbl_nome = tk.Label(self.frm_dados_cli, text='Name:', font=('Arial', 15))
        self.lbl_nome.grid(row=0, column=0, pady=20)
        self.ent_name = tk.Entry(self.frm_dados_cli, width=30, font=('Arial', 15), textvariable=self.nome_cli)
        self.ent_name.grid(row=0, column=1, pady=20)

        self.lbl_endereco = tk.Label(self.frm_dados_cli, text='Endereço:', font=('Arial', 15))
        self.lbl_endereco.grid(row=1, column=0, pady=20)
        self.ent_endereco = tk.Entry(self.frm_dados_cli, width=30, font=('Arial', 15), textvariable=self.endereco_cli)
        self.ent_endereco.grid(row=1, column=1, pady=20)

        self.lbl_cpf = tk.Label(self.frm_dados_cli, text='CPF:', font=('Arial', 15))
        self.lbl_cpf.grid(row=2, column=0, pady=20)
        self.ent_cpf = tk.Entry(self.frm_dados_cli, width=30, font=('Arial', 15), show='*', textvariable=self.cpf_cli)
        self.ent_cpf.grid(row=2, column=1, pady=20)

        # Botões
        self.btn_salvar = tk.Button(self.frm_botoes_cli, text='Salvar', width=10, height=1, font=10, bg="#50fa7d",
                                    activebackground='#0afa49', command=self.salvar_cli)
        self.btn_salvar.grid(row=0, column=0, padx=5, pady=10)

        self.btn_voltar = tk.Button(self.frm_botoes_cli, text='Voltar', width=10, height=1, font=10, bg="#2798f5",
                                    activebackground='#0525f7', command=self.voltar_cli)
        self.btn_voltar.grid(row=0, column=1, padx=5, pady=10)

    def salvar_cli(self):
        nome = self.nome_cli.get()
        endereco = self.endereco_cli.get()
        cpf = self.cpf_cli.get()

        if nome.strip() == '' or endereco.strip() == '' or cpf.strip() == '':
            messagebox.showinfo('Aviso', 'Preencha todos os campos!')
        else:
            # Criando uma instância da classe Cliente com os dados cadastrados
            novo_cliente = Cliente(nome, endereco, cpf)

            # Adicionando o novo cliente à lista de clientes cadastrados
            self.clientes_cadastrados.append(novo_cliente)

            self.top_cliente.destroy()
            self.home_page()

    def voltar_cli(self):
        self.top_cliente.destroy()
        self.home_page()

    ####### CADASTRO CLIENTES ########

    ####### TABELA DE CLIENTES ########
    def tabela(self):
        self.top_home_page.destroy()
        self.top_tabela_cli = tk.Toplevel(self.janela)

        self.frm_tabela = tk.Frame(self.top_tabela_cli)
        self.frm_tabela.pack()
        self.frm_botoes_tab = tk.Frame(self.top_tabela_cli)
        self.frm_botoes_tab.pack()

        # Tabela
        colunas = ('nome', 'endereco', 'cpf')
        self.tvw = ttk.Treeview(self.frm_tabela, columns=colunas, height=5, show='headings')
        self.tvw.grid()

        # Cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('endereco', text='Endereço')
        self.tvw.heading('cpf', text='CPF')

        # Colunas
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('endereco', minwidth=300, width=300)
        self.tvw.column('cpf', minwidth=150, width=150)

        # Linhas
        for cliente in self.clientes_cadastrados:
            self.tvw.insert('', 'end', values=(cliente._Cliente__nome, cliente._Cliente__endereco, cliente._Cliente__cpf))

        # Linhas


####### TABELA DE CLIENTES ########


app = tk.Tk()
Tela(app)
app.mainloop()
