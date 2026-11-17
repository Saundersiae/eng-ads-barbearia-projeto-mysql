import customtkinter as ctk
from tkinter import messagebox
from controllers.cliente_controller import ClienteController
from repositories.servico_repository import ServicosRepository

ctk.set_appearance_mode("dark")

class ClienteView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = ClienteController()
        self.servico_repo = ServicosRepository()

        self.title("Barbearia - Gerenciamento de Clientes")
        self.geometry("680x600")

        # _ CAMPO ID DO CLIENTE----------------------------------
        self.lbl_id = ctk.CTkLabel(self, text="ID do Cliente (apenas para alterar/excluir):")
        self.lbl_id.pack(pady=2)
        self.txt_id = ctk.CTkEntry(self, width=200, placeholder_text="Ex:1")
        self.txt_id.pack(pady=2)

        # _ CAMPO NOME -------------------------------------------
        self.lbl_nome = ctk.CTkLabel(self, text="Nome do Cliente:")
        self.lbl_nome.pack(pady=2)
        self.txt_nome = ctk.CTkEntry(self, width=280, placeholder_text="Digite o nome completo")
        self.txt_nome.pack(pady=2)

        # _ CAMPO TELEFONE -----------------------------------------
        self.lbl_tel = ctk.CTkLabel(self, text="Telefone:")
        self.lbl_tel.pack(pady=2)
        self.txt_tel = ctk.CTkEntry(self,width=280, placeholder_text="(00) 00000-0000")
        self.txt_tel.pack(pady=2)

        # _ CAMPO ID DO SERVICO ----------------------------------------
        self.lbl_servico = ctk.CTkLabel(self, text="ID do Serviço desejado:")
        self.lbl_servico.pack(pady=2)
        self.txt_servico = ctk.CTkEntry(self, width=280, placeholder_text="Olhe o número do ID na lista abaixo")
        self.txt_servico.pack(pady=2)

        # _ BOTÕES DO CRUD -------------------------------------
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=10)

        self.btn_salvar = ctk.CTkButton(self.frame_botoes, text="Salvar", width=100, command=self.cliclou_salvar)
        self.btn_salvar.pack(side="left", padx=5)

        self.btn_alterar = ctk.CTkButton(self.frame_botoes, text="Alterar", width=100, fg_color="orange",command=self.cliclou_alterar)
        self.btn_alterar.pack(side="left", pady=5)

        self.btn_excluir = ctk.CTkButton(self,self.frame_botoes, text="Excluir", width=100, fg_color="red", command=self.clicou_excluir)
        self.btn_excluir.pack(side="left", padx=5)

        # _ LISTA DE SERVIÇOS DISPONIVEIS ------------------------------
        self.lbl_listar_serv = ctk.CTkLabel(self, text="Serviços Disponiveis (ID - Nome - Preço):", font=("Arial", 12, "bold"))
        self.lbl_listar_serv.pack(pady=2)
        self.scroll_servicos = ctk.CTkScrollableFrame(self, width=550, height=85)
        self.scroll_servicos.pack(pady=2)

        # _ LISTA DE CLIENTES CADASTRADOS -----------------------------
        self.lbl_listar_cli = ctk.CTkLabel(self, text="Clientes Cadastrados:", font=("Arial", 12, "bold"))
        self.lbl_listar_cli.pack(pady=2)
        self.scroll_clientes = ctk.CTkScrollableFrame(self, width=550, height=120)
        self.scroll_clientes.pack(pady=2)

        self.carregar_servicos()
        self.carregar_clientes()

    def carregar_servicos(self):
        for widget in self.scroll_servicos.winfo_children():
            widget.destroy()
        try:
            servicos = self.servico_repo.listar_todos()
            for s in servicos:
                texto = f"ID: {s[0]} ---- serviço: {s[1]} ---- valor: R$ {s[2]}"
                ctk.CTkLabel(self.scroll_servicos, text=texto).pack(anchor="w", padx=10)
        except Exception as erro:
            ctk.CTkLabel(self.scroll_servicos, text=f"Erro ao carregar serviços: {erro}").pack()

    def carregar_clientes(self):
        for widget in self.scroll_clientes.winfo_children():
            widget.destroy()
        try:
            clientes = self.controller.listar_clientes()
            for c in clientes:
                texto = f"ID: {c[0]} ---- nome: {c[1]} ---- tel: {c[2]} ---- ID serviço: {c[3]}"
                ctk.CTkLabel(self.scroll_clientes, text=texto).pack(anchor="w", pady=10)
        except Exception as erro:
            ctk.CTkLabel(self.scroll_clientes, text=f"Erro ao listar clientes: {erro}").pack()

    def limpar_campos(self):
        self.txt_id.delete(0, 'end')
        self.txt_nome.delete(0, 'end')
        self.txt_tel.delete(0, 'end')
        self.txt_servico.delete(0, 'end')

    def clicou_salvar(self):
        nome = self.txt_nome.get()
        telefone = self.txt_tel.get()
        servicos_id = self.txt_servico.get()
        try:
            self.controller.cadastrar_novo_cliente(nome, telefone, servicos_id)
            messagebox.showinfo("Sucesso", "Cliente Cadastrado!")
            self.limpar_campos()
            self.carregar_clientes()
        except ValueError as erro:
            messagebox.showwarning("Aviso", str(erro))
        except Exception as erro:
            messagebox.showerror("erro", f"erro no banco: {erro}")

    def cliclou_alterar(self):
        id_cli = self.txt_nome.get()
        nome = self.txt_nome.get()
        telefone = self.txt_tel.get()
        servicos_id = self.txt_servico.get()
        try:
            self.controller.alterar_cliente(id_cli, nome, telefone, servicos_id)
            messagebox.showinfo("sucesso!", "cliente atualizado!")
            self.limpar_campos()
            self.carregar_clientes()
        except ValueError as erro:
            messagebox.showwarning("aviso", str(erro))
        except Exception as erro:
            messagebox.showerror("erro", f"erro ao atualizar: {erro}")

    def cliclou_excluir(self):
        id_cli = self.txt_id.get()
        try:
            self.controller.excluir_cliente(id_cli)
            messagebox.showinfo("sucesso", "clientes excluido")
            self.limpar_campos()
            self.carregar_clientes()
        except ValueError as erro:
            messagebox.showwarning("aviso", str(erro))
        except Exception as erro:
            messagebox.showerror("erro", f"erro ao excluir: {erro}")