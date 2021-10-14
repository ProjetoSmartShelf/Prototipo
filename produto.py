from configuracoes import Config
from cadastro import Cadastrar
from tkinter import *
from tkinter import ttk
import sqlite3

class Produtos(Toplevel):
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
        self.title('Produtos')
        self.geometry('390x656+1500+300')
        self.configure(background=self.color_blue)
        self.resizable(False, False)
        self.frames()
        self.tree()
        self.select_produtos()

        # Label
        Label(self,
            text = 'SmartShelf - Produtos',
            background = self.color_blue,
            foreground = self.color_black,
            font = ('Arial', 16)
        ).place(
            relheight = 0.05,
            relwidth = 0.52,
            relx = 0.03,
            rely = 0.03
        )

        # Label 2
        Label(self,
            text = 'Produtos cadastrados',
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
            font = ('Arial', 12, 'bold')
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
            font = ('Arial', 12),
            command = self.click_button_cadastro
        )

        self.button_cadastro.place(
            relheight = 0.05,
            relwidth = 0.40,
            relx = 0.57,
            rely = 0.10
        )


    def frames(self):
        ##### Textos lista de produtos #####
        # Lista de produtos
        self.frame_listaProdutos = Frame(
            self,
            background = self.color_blue,
            relief = SOLID,
            border = 1
        )
        self.frame_listaProdutos.place(
            relheight = 0.65,
            relwidth = 0.98,
            relx = 0.01,
            rely = 0.32
        )

        """     
        # Texto Código
        Label(self.frame_listaProdutos,
        text = 'Código',
        background = self.color_blue,
        foreground = self.color_black,
        font = ('', 12, 'bold')
        ).place(
            relheight = 0.05,
            relwidth = 0.30,
            relx = 0.01,
            rely = 0.02
        )
    
        # Texto Produto
        Label(self.frame_listaProdutos,
        text = 'Produto',
        background = self.color_blue,
        foreground = self.color_black,
        font = ('', 12, 'bold')
        ).place(
            relheight = 0.05,
            relwidth = 0.30,
            relx = 0.35,
            rely = 0.02
        )

       # Texto Quantidade
        Label(self.frame_listaProdutos,
        text = 'Quantidade',
        background = self.color_blue,
        foreground = self.color_black,
        font = ('', 12, 'bold')
        ).place(
            relheight = 0.05,
            relwidth = 0.30,
            relx = 0.69,
            rely = 0.02
        )
        """


    def tree(self):
        self.listaProdutos = ttk.Treeview(self.frame_listaProdutos, height = 3, column = ("col1", "col2", "col3"))
        self.listaProdutos.place(relheight = 0.98, relwidth = 0.98, relx = 0.01, rely = 0.01)

        self.listaProdutos.heading("#0", text="")
        self.listaProdutos.heading("#1", text="Código")
        self.listaProdutos.heading("#2", text="Produto")
        self.listaProdutos.heading("#3", text="Quantidade")

        self.listaProdutos.column("#0", stretch=YES, minwidth = 0, width = 0, anchor="center")
        self.listaProdutos.column("#1", stretch=YES, minwidth = 125, width = 30, anchor="center")
        self.listaProdutos.column("#2", stretch=YES, minwidth = 125, width = 30, anchor="center")
        self.listaProdutos.column("#3", stretch=YES, minwidth = 125, width = 30, anchor="center")
    

    def select_produtos(self):
        self.produtos = [
            ["1", "Produto 1", 5],
            ["2", "Produto 2", 8],
            ["3", "Produto 3", 2],
            ["4", "Produto 4", 0],
            ["5", "Produto 5", 9],
            ]
    
        for i in self.produtos:
            self.listaProdutos.insert("",END, values=i)




    # Configurações
    def click_button_config(self):
        self.hide()
        self.subFrame = Config(self)
    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

    # Cadastro
    def click_button_cadastro(self):
        self.hide()
        self.subFrame = Cadastrar(self)
    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()


    def widgets_frameProdutos(self):
        pass
    

