import customtkinter as ctk
from tkinter import messagebox
from controllers.cliente_controller import ClienteController

ctk.set_appearance_mode("dark")

class ClienteView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = ClienteController()

        self.title("Barbearia - Cadastro de Clientes")
        self.geometry("400x350")

        self.lbl_nome = ctk.CTkLabel(self, text="Nome do Cliente:")
        self.lbl_nome.pack(pady=5)
        self.txt_nome = ctk.CTkEntry(self, width=250, placeholder_text="Digite o nome completo")
        self.txt_nome.pack(pady=5)

        self.lbl_tel = ctk.CTkLabel(self, text="Telefone:")
        self.lbl_tel.pack(pady=5)
        self.txt_tel = ctk.CTkEntry(self, width=250, placeholder_text="(00) 0000-0000")
        self.txt_tel.pack(pady=5)

        self.bnt_salvar = ctk.CTkButton(self, text="Salvar Cadastro", command=self.clicou_no_botao)
        self.bin_salvar.pack(pady=20)

def clicou_no_botao(self):
    nome = self.txt_nome.get()
    telefone = self.txt_tel.get()

    try:
        self.controller.cadastrar_novo_cliente(nome, telefone)
        messagebox.showinfo("sucesso!", "Cliente Cadastrado no banco da barbearia!")

        self.txt_nome.delete(0, 'end')
        self.txt_tel.delete(0, 'end')

    except ValueError as erro_validacao:
        messagebox.showwarning("aviso", str(erro_validacao))
    except Exception as erro_banco:
        messagebox.showerror("erro", f"não consegui conectar ao MySQL: {str(erro_banco)}")