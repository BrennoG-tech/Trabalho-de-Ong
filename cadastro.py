import tkinter as tk
from tkinter import messagebox
import banco
from main import tela_login, limpar_janela

def tela_cadastro(janela):
    limpar_janela(janela)
    tk.Label(janela, text="Cadastro de Usuário", font=("Arial", 25, "bold")).pack(pady=20)

    tk.Label(janela, text="Nome:").pack()
    nome = tk.Entry(janela)
    nome.pack()

    tk.Label(janela, text="Sobrenome:").pack()
    sobrenome = tk.Entry(janela)
    sobrenome.pack()

    tk.Label(janela, text="Email:").pack()
    email = tk.Entry(janela)
    email.pack()

    tk.Label(janela, text="Nome de Usuário:").pack()
    usuario = tk.Entry(janela)
    usuario.pack()

    tk.Label(janela, text="Senha:").pack()
    senha = tk.Entry(janela, show="*")
    senha.pack()

    def salvar_usuario():
        if not (nome.get() and sobrenome.get() and email.get() and usuario.get() and senha.get()):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        sucesso = banco.cadastrar_usuario(
            nome.get(),
            sobrenome.get(),
            email.get(),
            usuario.get(),
            senha.get()
        )

        if sucesso:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            tela_login(janela)
        else:
            messagebox.showerror("Erro", "Email ou nome de usuário já cadastrado.")

    tk.Button(janela, text="Salvar", width=15, command=salvar_usuario).pack(pady=10)
    tk.Button(janela, text="Voltar", width=15, command=lambda: tela_login(janela)).pack()