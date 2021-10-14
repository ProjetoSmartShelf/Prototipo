from tkinter import *
from tkinter import messagebox
import sqlite3

class Criarconta(Toplevel):
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
        self.title('Criar conta')
        self.geometry('390x656+1500+300')
        self.configure(background=self.color_blue)
        self.resizable(False, False)

        # Button voltar
        self.imagem_botao_voltar = PhotoImage(file = 'images/icon_voltar.png')
        self.botao_voltar = Button(self, 
        image = self.imagem_botao_voltar, 
        background = self.color_blue,
        activebackground = self.color_blue,
        relief = SOLID,
        border = 0,
        command = self.voltar
        )

        self.botao_voltar.place(relheight =0.07, 
        relwidth = 0.10, 
        relx =0.90, 
        rely =0.02
        )

        # Label 
        Label(self,
            text = 'Criando uma conta',
            background = self.color_gray,
            foreground = self.color_blue,
            borderwidth = 1,
            relief = SOLID,
            font = ('Arial', 12, 'bold')
        ).place(
            relheight = 0.05,
            relwidth = 0.98,
            relx = 0.01,
            rely = 0.85
        )

        # Text criar email
        Label(self,
            text = 'Email',
            background = self.color_blue,
            foreground = self.color_black
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.275
            )

        # Entry criar email
        self.entry_criarEmail = Entry(
            self,
            relief=SOLID
        )

        self.entry_criarEmail.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.30,
        )

        # Text usuario
        Label(self,
            text = 'Usuário',
            background = self.color_blue,
            foreground = self.color_black
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.355
            )

        # Entry criar usuario
        self.entry_criarUsuario = Entry(
            self,
            relief=SOLID
        )

        self.entry_criarUsuario.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.38,
        )

        # Text cpf
        Label(self,
            text = 'CPF',
            background = self.color_blue,
            foreground = self.color_black,
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.435
            )

        # Entry criar cpf
        self.entry_criarCPF = Entry(
            self,
            relief=SOLID
        )

        self.entry_criarCPF.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.46,
        )

        # Text criar senha
        Label(self,
            text = 'Senha',
            background = self.color_blue,
            foreground = self.color_black
            ).place(
                relheight = 0.03,
                relwidth = 0.12,
                relx = 0.44,
                rely = 0.515
            )

        # Entry criar senha
        self.entry_criarSenha = Entry(
            self,
            show = '*',
            relief=SOLID
        )

        self.entry_criarSenha.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.54,
        )

        # Text repetir senha
        Label(self,
            text = 'Repetir senha',
            background = self.color_blue,
            foreground = self.color_black
            ).place(
                relheight = 0.03,
                relwidth = 0.20,
                relx = 0.40,
                rely = 0.595
            )

        # Entry repetir senha
        self.entry_criarSenha2 = Entry(
            self,
            show = '*',
            relief=SOLID
        )

        self.entry_criarSenha2.place(
            relheight = 0.04,
            relwidth = 0.36,
            relx = 0.32,
            rely = 0.62,
        )

       # BUTTON Confirmar
        self.button_confirmarCriacaoConta = Button(
            self,
            text = 'Confirmar',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief = SOLID,
            font = ('Arial', 10),
            command = self.cadastrar
        )

        self.button_confirmarCriacaoConta.place(
            relheight = 0.04,
            relwidth = 0.28,
            relx = 0.36,
            rely = 0.70
        )

        # Button ocultar senha
        self.imagem_botao_ocultarSenha = PhotoImage(file = 'images/icon_naovisivel.png')
        self.button_ocultarSenha = Button(
            self,
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
            rely = 0.54
        )
            
    # Método para voltar
    def voltar(self):
        self.respostaVoltar = messagebox.askquestion('Voltar', 'Você deseja Voltar?')

        if self.respostaVoltar == 'yes':
            print('Voltando')
            self.destroy()
            self.frame_original.show()
        
        else:
            print('Volta cancelada')
    
    # Método para mostrar/ocutar senha
    def mostrarSenha(self):
        self.entry_criarSenha['show'] = '*'
        self.entry_criarSenha2['show'] = '*'
        self.imagem_botao_ocultarSenha = PhotoImage(file = 'images/icon_naovisivel.png')
        self.button_ocultarSenha = Button(
            self,
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
            rely = 0.54
        )

    def mostrarSenha2(self):
        self.entry_criarSenha['show'] = ''
        self.entry_criarSenha2['show'] = ''
        self.imagem_botao_ocultarSenha = PhotoImage(file = 'images/icon_visivel.png')
        self.button_ocultarSenha = Button(
            self,
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
            rely = 0.54
        )



    ########## Banco de dados Cadastro ##########
    def cadastrar(self):
        # Capturar os dados
        self.capturaDados_email = self.entry_criarEmail.get()
        self.capturaDados_usuario = self.entry_criarUsuario.get()
        self.capturaDados_cpf = self.entry_criarCPF.get()
        self.capturaDados_senha = self.entry_criarSenha.get()
        self.capturaDados_senha2 = self.entry_criarSenha2.get()

        # Limpar as caixas de texto
        self.entry_criarEmail.delete(0, 'end')
        self.entry_criarUsuario.delete(0, 'end')
        self.entry_criarCPF.delete(0, 'end')
        self.entry_criarSenha.delete(0, 'end')
        self.entry_criarSenha2.delete(0, 'end')


        if self.capturaDados_email == '' and self.capturaDados_usuario == '' and self.capturaDados_cpf == '' and self.capturaDados_senha == '' and self.capturaDados_senha2 == '':
            print('Tudo vazio')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')
        
        elif self.capturaDados_email == '':
            print('Email vazio')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')

        elif self.capturaDados_usuario == '':
            print('Usuario vazio')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')

        elif self.capturaDados_cpf == '':
            print('CPF vazio')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')

        elif self.capturaDados_senha == '':
            print('Senha vazia')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')

        elif self.capturaDados_senha2 == '':
            print('Senha 2 vazia')
            messagebox.showerror('Erro', 'É necessário preencher todos os campos!')
        
        else:
            if (self.capturaDados_senha == self.capturaDados_senha2):
                try:
                    self.banco_cadastro = sqlite3.connect('cadastro.db')
                    self.cursor_cadastro = self.banco_cadastro.cursor()
                    self.cursor_cadastro.execute("CREATE TABLE IF NOT EXISTS cadastro (email VARCHAR(50), usuario VARCHAR(30), cpf VARCHAR(20), senha VARCHAR(30))")
                    self.cursor_cadastro.execute("INSERT INTO cadastro VALUES ('"+self.capturaDados_email+"','"+self.capturaDados_cpf+"','"+self.capturaDados_usuario+"','"+self.capturaDados_senha+"')")

                    self.banco_cadastro.commit()
                    
                    self.cursor_cadastro.execute("SELECT * FROM cadastro")
                    print(self.cursor_cadastro.fetchall())
                    
                    self.banco_cadastro.close()
                    
                    print('Tudo certo')
                    messagebox.showinfo('Usuário cadastrado', 'Usuário cadastrado com sucesso!')
                    

                except sqlite3.Error as erro:
                    print(f'Erro ao inserir os dados: {erro}')
            
            else:
                messagebox.showerror('Erro', 'As duas senhas não correspondem')


    ##### Validação dos dados para login #####



classe = Criarconta