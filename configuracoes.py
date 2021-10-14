from tkinter import *
from tkinter import messagebox

class Config(Toplevel):
    # Colors
    color_blue = '#523BFF'
    color_blue2 = '#007EC4'
    color_white = '#FCF7FF'
    color_black = '#1E1927'

    def __init__(self, original):
        self.frame_original = original

        # Constructor Method
        Toplevel.__init__(self)
        self.title('Configurações')
        self.geometry('390x656+1500+300')
        self.configure(background=self.color_blue)
        self.resizable(False, False)

        # Label
        Label(self,
            text = 'Configurações',
            background = self.color_blue,
            foreground = self.color_black,
            font = ('Arial', 16)
        ).place(
            relheight = 0.05,
            relwidth = 0.38,
            relx = 0.01,
            rely = 0.03
        )

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

        # Button Sair
        self.button_sair = Button(
            self,
            text = 'Sair',
            background = self.color_blue2,
            activebackground = self.color_blue2,
            foreground = self.color_black,
            activeforeground = self.color_black,
            border = 1,
            relief = SOLID,
            font = ('Arial', 10),
            command = self.sair
        )

        self.button_sair.place(
            relheight = 0.04,
            relwidth = 0.28,
            relx = 0.36,
            rely = 0.30
        )

    # Método para voltar
    def voltar(self):
        self.destroy()
        self.frame_original.show()

    # Método para sair
    def sair(self):
        self.respostaSair = messagebox.askquestion('Sair','Você deseja sair?')
        
        if self.respostaSair == 'yes':
            print('Saindo')
            self.destroy()
        
        else:
            print('Saída cancelada')
