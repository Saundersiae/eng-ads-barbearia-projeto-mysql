import customtkinter as ctk
from tkinter import messagebox, ttk
from controllers.cliente_controller import ClienteController


class ClienteView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.controller = ClienteController()
        self.title("Gerenciamento da Barbearia")
        self.geometry("900x850")
        ctk.set_appearance_mode("dark")

        self.criar_tela()
        self.listar_clientes()

    def criar_tela(self):
        ctk.CTkLabel(
            self,
            text="GERENCIAMENTO DE CLIENTES",
            font=("Arial", 24, "bold"),
            text_color="white"
        ).pack(pady=10)

        # Cadastro do cliente
        cadastro = ctk.CTkFrame(self, fg_color="gray20")
        cadastro.pack(padx=20, pady=5, fill="x")

        ctk.CTkLabel(
            cadastro,
            text="Cadastrar Cliente",
            font=("Arial", 18, "bold"),
            text_color="white"
        ).pack(pady=10)

        ctk.CTkLabel(cadastro, text="Nome:").pack()
        self.nome = ctk.CTkEntry(cadastro, width=250)
        self.nome.pack(pady=5)

        ctk.CTkLabel(cadastro, text="Telefone:").pack()
        self.telefone = ctk.CTkEntry(cadastro, width=250)
        self.telefone.pack(pady=5)

        ctk.CTkLabel(cadastro, text="ID do serviço:").pack()
        self.servico = ctk.CTkEntry(cadastro, width=250)
        self.servico.pack(pady=5)

        ctk.CTkButton(
            cadastro,
            text="Cadastrar",
            fg_color="#7138A8",
            command=self.cadastrar
        ).pack(pady=10)

        # Gerenciamento dos clientes
        gerenciamento = ctk.CTkFrame(self, fg_color="gray20")
        gerenciamento.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(
            gerenciamento,
            text="Gerenciar Clientes",
            font=("Arial", 18, "bold"),
            text_color="white"
        ).pack(pady=10)

        ctk.CTkLabel(
            gerenciamento,
            text="ID do cliente:"
        ).pack(pady=5)

        self.id = ctk.CTkEntry(gerenciamento, width=250)
        self.id.pack(pady=5)

        ctk.CTkButton(
            gerenciamento,
            text="Alterar",
            fg_color="#7138A8",
            command=self.alterar
        ).pack(pady=5)

        ctk.CTkButton(
            gerenciamento,
            text="Excluir",
            fg_color="#C0392B",
            command=self.excluir
        ).pack(pady=5)

        ctk.CTkButton(
            gerenciamento,
            text="Atualizar lista",
            fg_color="#2874A6",
            command=self.listar_clientes
        ).pack(pady=5)

        # Tabela de clientes
        self.tabela = ttk.Treeview(
            self,
            columns=("id", "nome", "telefone", "servico", "data"),
            show="headings"
        )
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("telefone", text="Telefone")
        self.tabela.heading("servico", text="Serviço")
        self.tabela.heading("data", text="Data")

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

    def cadastrar(self):
        nome = self.nome.get()
        telefone = self.telefone.get()
        servico = self.servico.get()

        try:
            self.controller.cadastrar_novo_cliente(
                nome, telefone, servico
            )
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")
            self.limpar()
            self.listar_clientes()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def listar_clientes(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        try:
            clientes = self.controller.listar_clientes()
            for cliente in clientes:
                self.tabela.insert("", "end", values=cliente[:5])
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def alterar(self):
        id_cliente = self.id.get()
        nome = self.nome.get()
        telefone = self.telefone.get()
        servico = self.servico.get()

        if not id_cliente.isdigit():
            messagebox.showwarning("Atenção", "Digite um ID válido.")
            return

        try:
            resultado = self.controller.alterar_cliente(
                id_cliente, nome, telefone, servico
            )
            if resultado == 0:
                messagebox.showwarning("Atenção", "Cliente não encontrado.")
            else:
                messagebox.showinfo("Sucesso", "Cliente alterado!")
                self.limpar()
                self.listar_clientes()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):
        id_cliente = self.id.get()

        if not id_cliente.isdigit():
            messagebox.showwarning("Atenção", "Digite um ID válido.")
            return

        resposta = messagebox.askyesno(
            "Excluir",
            "Deseja excluir esse cliente?"
        )
        if resposta:
            try:
                resultado = self.controller.excluir_cliente(id_cliente)
                if resultado == 0:
                    messagebox.showwarning("Atenção", "Cliente não encontrado.")
                else:
                    messagebox.showinfo("Sucesso", "Cliente excluído!")
                    self.limpar()
                    self.listar_clientes()
            except Exception as erro:
                messagebox.showerror("Erro", str(erro))

    def limpar(self):
        self.id.delete(0, "end")
        self.nome.delete(0, "end")
        self.telefone.delete(0, "end")
        self.servico.delete(0, "end")


if __name__ == "__main__":
    app = ClienteView()
    app.mainloop()
