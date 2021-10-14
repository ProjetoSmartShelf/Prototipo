from tkinter import *
from tkinter import messagebox
from produto import Produtos
from registro_conta import *

# Login Window
class Login(Criarconta):
    # Colors
    color_blue = '#523BFF'
    color_blue2 = '#007EC4'
    color_white = '#FCF7FF'
    color_black = '#1E1927'
    color_gray = '#303030'
    
    # Constructor Method
    def __init__(self):
        self.root = root
        self.login_settings()
        self.login_logo()
        self.login_entry()
        self.login_buttons()
        self.mostrarSenha()

        self.root.mainloop()

    # Login Screen Settings
    def login_settings(self):
        self.root.title('Login')
        self.root.geometry('390x656+1500+300')
        self.root.configure(background=self.color_blue)
        self.root.resizable(False, False)

    # Logo
    def login_logo(self):
        pass

    # Entrys
    def login_entry(self):
        # Text Usuário
        Label(self.root,
            text = 'Usuário',
            background = self.color_blue,
            foreground = self.color_black,
            
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.375
            )

        # ENTRY USUÁRIO
        self.entry_usuario = Entry(
            self.root,
            relief=SOLID
        )

        self.entry_usuario.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.40,
        )

        # Text Senha
        Label(self.root,
            text = 'Senha',
            background = self.color_blue,
            foreground = self.color_black,
            
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.455
            )

        # ENTRY SENHA
        self.visualizarSenha = '*'
        self.entry_senha = Entry(
            self.root,
            show = '*',
            relief=SOLID
        )

        self.entry_senha.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.48,
        )

    # Buttons
    def login_buttons(self):
        # BUTTON ENTRAR
        self.login_button_entrar = Button(
            self.root,
            text = 'Entrar',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief = SOLID,
            font = ('Arial', 10),
            command = self.validarDados
        )

        self.login_button_entrar.place(
            relheight = 0.04,
            relwidth = 0.28,
            relx = 0.36,
            rely = 0.56
        )

        # BUTTON REGISTRAR
        self.login_button_registrar = Button(
            self.root,
            text = 'Registrar',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief=SOLID,
            font = ('Arial', 10),
            command = self.click_button_registrar
        )

        self.login_button_registrar.place(
            relheight = 0.04,
            relwidth = 0.24,
            relx = 0.38,
            rely = 0.62
        )

        """
        # BUTTON Recuperar senha
        self.login_button_recuperarSenha = Button(
            self.root,
            text = 'Recuperar senha',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief=SOLID,
            font = ('Arial', 10)
        )

        self.login_button_recuperarSenha.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.90
        )
        """
    
    def mostrarSenha(self):
        # Button ocultar senha
        self.entry_senha['show'] = '*'
        self.imagem_botao_ocultarSenha = PhotoImage(file = 'images/icon_naovisivel.png')
        self.button_ocultarSenha = Button(
            self.root,
            image = self.imagem_botao_ocultarSenha,
            background = self.color_blue,
            activebackground = self.color_blue,
            relief = SOLID,
            border = 1,
            command = self.mostrarSenha2
        )
        
        self.button_ocultarSenha.place(
            relheight = 0.04,
            relwidth = 0.10,
            relx = 0.70,
            rely = 0.48
        )

    def mostrarSenha2(self):
        # Button mostrar senha
        self.entry_senha['show'] = ''
        self.imagem_botao_ocultarSenha = PhotoImage(file = 'images/icon_visivel.png')
        self.button_ocultarSenha = Button(
            self.root,
            image = self.imagem_botao_ocultarSenha,
            background = self.color_blue,
            activebackground = self.color_blue,
            relief = SOLID,
            border = 1,
            command = self.mostrarSenha
        )
        
        self.button_ocultarSenha.place(
            relheight = 0.04,
            relwidth = 0.10,
            relx = 0.70,
            rely = 0.48
        )

    def click_button_entrar(self):
        self.hide()
        self.subFrame = Produtos(self)
    def hide(self):
        self.root.withdraw
    def show(self):
        self.root.update()
        self.root.deiconify()
    
    def click_button_registrar(self):
        self.hide()
        self.subFrame = Criarconta(self)
    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()

    # Validar dados
    def validarDados(self):
        self.banco_cadastro = sqlite3.connect('cadastro.db')
        self.cursor_cadastro = self.banco_cadastro.cursor()

        self.cursor_cadastro.execute("SELECT * FROM cadastro")
        self.usuario_senha = self.cursor_cadastro.fetchall()

        print(self.usuario_senha)
        
        self.usuario = self.usuario_senha[0][2]
        self.senha = self.usuario_senha[0][3]
        print(self.usuario)
        print(self.senha)


        # Captura dos dados
        self.validarDados_usuario = self.entry_usuario.get()
        self.validarDados_senha = self.entry_senha.get()

        if self.validarDados_usuario == '' and self.validarDados_senha == '':
            print('Está tudo vazio')
            messagebox.showerror('Erro', 'Digite seu usuário e senha!')
        
        elif self.validarDados_usuario == '':
            print('Usuário vazio')
            messagebox.showerror('Erro', 'Digite seu usuário!')
            self.entry_senha.delete(0, 'end')
        
        elif self.validarDados_senha == '':
            print('Senha vazia')
            messagebox.showerror('Erro', 'Digite sua senha!')
            self.entry_usuario.delete(0, 'end')
        
        elif self.validarDados_usuario == self.usuario and self.validarDados_senha == self.senha:
            print('Login feito')
            self.click_button_entrar()
        
        else:
            print('Usuário ou senha incorretos')
            messagebox.showerror('Erro', 'Usuário ou senha incorretos!')
            self.entry_usuario.delete(0, 'end')
            self.entry_senha.delete(0, 'end')


    ##### Validação dos dados para login #####
    def validarDadosLogin(self):
        self.banco_cadastro = sqlite3.connect('cadastro.db')
        self.cursor_cadastro = self.banco_cadastro.cursor()

        self.cursor_cadastro.execute("SELECT * FROM cadastro")
        self.usuario_senha = self.cursor_cadastro.fetchall()

        print(self.usuario_senha)
        
        self.usuario = self.usuario_senha[0][2]
        self.senha = self.usuario_senha[0][3]
        print(self.usuario)
        print(self.senha)

root = Tk()
Login()
