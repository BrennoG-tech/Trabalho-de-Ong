import tkinter as tk
from tkinter import messagebox
import banco
from main import abrir_menu, limpar_janela, tela_cadastro

def login(janela, entrada_usuario, entrada_senha):
    nome_usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if nome_usuario and senha:
        nome_real = banco.validar_login(nome_usuario, senha)
        if nome_real:
            abrir_menu(janela, nome_real)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

def tela_login(janela):
    limpar_janela(janela)
    tk.Label(janela, text="Login", font=("Arial", 25, "bold")).pack(pady=20)

    tk.Label(janela, text="Nome de Usuário:").pack()
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.pack()

    tk.Label(janela, text="Senha:").pack()
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack()

    tk.Button(janela, text="Entrar", width=15, command=lambda: login(janela, entrada_usuario, entrada_senha)).pack(pady=10)
    tk.Button(janela, text="Cadastrar", width=15, command=lambda: tela_cadastro(janela)).pack()