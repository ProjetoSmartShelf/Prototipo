import sqlite3
from configuracoes import Config
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from produto import *

class Cadastrar(Toplevel):
    # Colors
    color_blue = '#523BFF'
    color_blue2 = '#007EC4'
    color_white = '#FCF7FF'
    color_black = '#1E1927'
    color_gray = '#303030'

    def __init__(self, original):
        self.frame_original = original

        # Constructor Method
        Toplevel.__init__(self)
        self.title('Cadastro de produtos')
        self.geometry('390x656+1500+300')
        self.configure(background=self.color_blue)
        self.resizable(False, False)

        # Label
        Label(self,
            text = 'SmartShelf - Cadastro',
            background = self.color_blue,
            foreground = self.color_black,
            font = ('Arial', 16)
        ).place(
            relheight = 0.05,
            relwidth = 0.55,
            relx = 0.02,
            rely = 0.03
        )

        # Label 2
        Label(self,
            text = 'Cadastro de Produtos',
            background = self.color_gray,
            foreground = self.color_blue,
            borderwidth = 1,
            relief = SOLID,
            font = ('Arial', 12, 'bold')
        ).place(
            relheight = 0.05,
            relwidth = 0.98,
            relx = 0.01,
            rely = 0.25
        )

        # Button configurações        
        self.imagem_botao_config = PhotoImage(file = 'images/icon_configuracao.png')
        self.botao_config = Button(self, 
        image = self.imagem_botao_config, 
        background = self.color_blue,
        activebackground = self.color_blue,
        relief = SOLID,
        border = 0,
        command = self.click_button_config
        )

        self.botao_config.place(relheight =0.05, 
        relwidth = 0.09, 
        relx =0.90, 
        rely =0.03
        )

        # Button Produto
        self.button_produtos = Button(
            self,
            text = 'Produtos',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief=SOLID,
            font = ('Arial', 12),
            command = self.voltar_produtos
        )

        self.button_produtos.place(
            relheight = 0.05,
            relwidth = 0.40,
            relx = 0.03,
            rely = 0.10
        )

        # Button Cadastro
        self.button_cadastro = Button(
            self,
            text = 'Cadastro',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief=SOLID,
            font = ('Arial', 12, 'bold')
        )

        self.button_cadastro.place(
            relheight = 0.05,
            relwidth = 0.40,
            relx = 0.57,
            rely = 0.10
        )

        # Cadastro dos produtos
        # Texto nome do produto
        Label(self,
            text = 'Nome do produto',
            background = self.color_blue,
            foreground = self.color_black
        ).place(
            relheight = 0.05,
            relwidth = 0.30,
            relx = 0.35,
            rely = 0.40
        )

        # Entry nome do produto
        self.entry_nomeProduto = Entry(
            self,
            relief=SOLID
        )
        self.entry_nomeProduto.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.435
        )

        # Texto código do produto
        Label(self,
        text = 'O ID do produto\nserá inserido automaticamente',
        background = self.color_blue,
        foreground = self.color_black,
        font = ('', 10, 'bold'),
        relief = SOLID,
        border = 1
        ).place(
            relheight = 0.10,
            relwidth = 0.56,
            relx = 0.22,
            rely =  0.60
        )

        """
        # Entry código produto
        self.entry_idProduto = Entry(
            self,
            relief=SOLID
        )
        self.entry_idProduto.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.515
        )
        """

        # Botão Cadastrar
        self.button_cadastrarProduto = Button(
            self,
            text = 'Cadastrar',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief = SOLID,
            font = ('Arial', 10),
            command = self.cadastrarProdutos
        )

        self.button_cadastrarProduto.place(
            relheight = 0.04,
            relwidth = 0.28,
            relx = 0.36,
            rely = 0.50
        )


    # Método para voltar
    def voltar_produtos(self):
        self.destroy()
        self.frame_original.show()
        self.mostrarProdutos()

    # Configurações
    def click_button_config(self):
        self.hide()
        self.subFrame = Config(self)
    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

    # Guardando os produtos no banco de dados
    def cadastrarProdutos(self):
        print('Clicou em cadastrar')
        self.cadastrarProduto_nome = self.entry_nomeProduto.get()

        if self.cadastrarProduto_nome == '':
            print('Nome do produto vazio')
            messagebox.showerror('Erro', 'É preciso informar o nome do produto!')

        else:
            try:
                self.banco_cadastroProduto = sqlite3.connect('produto.db')
                self.cursor_cadastroProduto = self.banco_cadastroProduto.cursor()
                self.cursor_cadastroProduto.execute("CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY, nome_produto VARCHAR(30) NOT NULL)")
                self.cursor_cadastroProduto.execute("INSERT INTO produto (nome_produto) VALUES ('"+self.cadastrarProduto_nome+"')")

                self.banco_cadastroProduto.commit()

                self.cursor_cadastroProduto.execute("SELECT * FROM produto")
                print(self.cursor_cadastroProduto.fetchall())

                self.banco_cadastroProduto.close()

                print('Tudo certo')
                messagebox.showinfo('Produto cadastrado', 'Produto cadastrado com sucesso')

            except sqlite3.Error as erro:
                print(f'Erro ao inserir os dados: {erro}')

        self.entry_nomeProduto.delete(0, 'end')

    def mostrarProdutos(self):
        self.banco_cadastroProduto = sqlite3.connect('produto.db')
        self.cursor_cadastroProduto = self.banco_cadastroProduto.cursor()

        self.cursor_cadastroProduto.execute("SELECT * FROM produto")
        self.produtos_lidos = self.cursor_cadastroProduto.fetchall()
        print(self.produtos_lidos)

            




