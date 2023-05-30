import re
import sqlite3
import tkinter as tk
from tkinter import messagebox


# Função para criar a tabela de usuários no banco de dados
def criar_tabela_usuarios():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nome TEXT, email TEXT, telefone TEXT, senha TEXT)''')
    conn.commit()
    conn.close()


# Função para criar a tabela de produtos no banco de dados
def criar_tabela_produtos():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS produtos
                 (nome TEXT, quantidade INTEGER, marca TEXT)''')
    conn.commit()
    conn.close()


# Função para cadastrar um usuário no banco de dados
def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    senha = senha_entry.get()

    if not re.match("^[a-zA-Z ]+$", nome):
        mensagem.set("Erro: Nome inválido")
        return

    if not re.match("^\d{11}$", telefone):
        mensagem.set("Erro: Telefone inválido")
        return

    if not re.match("^[a-zA-Z0-9]{1,8}$", senha):
        mensagem.set("Erro: Senha inválida")
        return

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)", (nome, email, telefone, senha))
    conn.commit()
    conn.close()
    mensagem.set("Usuário cadastrado com sucesso")


def cadastrar_produto():
    nome_produto = produto_nome_entry.get()
    quantidade = produto_quantidade_entry.get()
    marca = produto_marca_entry.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos VALUES (?, ?, ?)", (nome_produto, quantidade, marca))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso!", text="Produto Cadastrado com Sucesso!")


def editar_produto():
    nome_produto = produto_nome_entry.get()
    quantidade = produto_quantidade_entry.get()
    marca = produto_marca_entry.get()

    if not nome_produto:
        messagebox.showerror("Erro", "Por favor, insira o nome do produto existente")
        return
    
    def salvar_edicao():
        novo_nome = novo_nome_entry.get()
        nova_quantidade = nova_quantidade_entry.get()
        nova_marca = nova_marca_entry.get()

        if not novo_nome or not nova_quantidade or not nova_marca:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE produtos SET nome = ?, quantidade = ?, marca = ? WHERE nome = ?",
                 (novo_nome, nova_quantidade, nova_marca, nome_produto))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
        edicao_janela.destroy()

    # Criar a janela de edição do produto
    edicao_janela = tk.Toplevel(window)
    edicao_janela.title("Editar Produto")
    edicao_janela.geometry("300x300")
    edicao_janela.resizable(height=False, width=False)

    # Criar os campos de entrada para a edição
    novo_nome_label = tk.Label(edicao_janela, text="Novo Nome:")
    novo_nome_label.pack()
    novo_nome_entry = tk.Entry(edicao_janela)
    novo_nome_entry.pack()

    nova_quantidade_label = tk.Label(edicao_janela, text="Nova Quantidade:")
    nova_quantidade_label.pack()
    nova_quantidade_entry = tk.Entry(edicao_janela)
    nova_quantidade_entry.pack()

    nova_marca_label = tk.Label(edicao_janela, text="Nova Marca:")
    nova_marca_label.pack()
    nova_marca_entry = tk.Entry(edicao_janela)
    nova_marca_entry.pack()

    # Botão para salvar as alterações
    salvar_button = tk.Button(edicao_janela, text="Salvar", command=salvar_edicao)
    salvar_button.pack()


# Função para fazer o login
def fazer_login():
    email = login_email_entry.get()
    senha = login_senha_entry.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    resultado = c.fetchone()
    conn.close()

    if resultado:
        tela_login.pack_forget()
        tela_produtos.pack()

        # Aqui você pode adicionar a lógica para exibir os produtos

    else:
        mensagem_login.set("Credenciais inválidas")

# Função para voltar à tela de login na tela de cadastro de usuário
def voltar_login_cadastro():
    tela_cadastro.pack_forget()
    tela_login.pack()

# Função para exibir a tela de cadastro de usuário
def exibir_tela_cadastro():
    tela_login.pack_forget()
    tela_cadastro.pack()

# Função para voltar à tela de login na tela de cadastro de produto
def voltar_login_produtos():
    tela_produtos.pack_forget()
    tela_login.pack()

# Função para exibir a tela de cadastro de produto
def exibir_tela_produtos():
    tela_login.pack_forget()
    tela_produtos.pack()

# Criar tabelas do banco de dados
criar_tabela_usuarios()
criar_tabela_produtos()

# Configuração da janela principal
window = tk.Tk()
window.title("Sistema de Login")
window.geometry("400x300")
window.resizable(height=False, width=False)

# Tela de login
tela_login = tk.Frame(window)

login_email_label = tk.Label(tela_login, text="Email:")
login_email_label.pack()
login_email_entry = tk.Entry(tela_login)
login_email_entry.pack()

login_senha_label = tk.Label(tela_login, text="Senha:")
login_senha_label.pack()
login_senha_entry = tk.Entry(tela_login, show="*")
login_senha_entry.pack()

mensagem_login = tk.StringVar()
mensagem_login_label = tk.Label(tela_login, textvariable=mensagem_login)
mensagem_login_label.pack()

login_button = tk.Button(tela_login, text="Login", command=fazer_login)
login_button.pack()

cadastro_button = tk.Button(tela_login, text="Cadastrar", command=exibir_tela_cadastro)
cadastro_button.pack()

tela_login.pack()

# Tela de cadastro
tela_cadastro = tk.Frame(window)

nome_label = tk.Label(tela_cadastro, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(tela_cadastro)
nome_entry.pack()

email_label = tk.Label(tela_cadastro, text="Email:")
email_label.pack()
email_entry = tk.Entry(tela_cadastro)
email_entry.pack()

telefone_label = tk.Label(tela_cadastro, text="Telefone (11 dígitos):")
telefone_label.pack()
telefone_entry = tk.Entry(tela_cadastro)
telefone_entry.pack()

senha_label = tk.Label(tela_cadastro, text="Senha (até 8 caracteres):")
senha_label.pack()
senha_entry = tk.Entry(tela_cadastro, show="*")
senha_entry.pack()

mensagem = tk.StringVar()
mensagem_label = tk.Label(tela_cadastro, textvariable=mensagem)
mensagem_label.pack()

cadastrar_usuario_button = tk.Button(tela_cadastro, text="Cadastrar", command=cadastrar_usuario)
cadastrar_usuario_button.pack()

voltar_button_cadastro = tk.Button(tela_cadastro, text="Voltar para o Login", command=voltar_login_cadastro)
voltar_button_cadastro.pack()

# Tela de produtos
tela_produtos = tk.Frame(window)

produto_nome_label = tk.Label(tela_produtos, text="Nome do Produto:")
produto_nome_label.pack()
produto_nome_entry = tk.Entry(tela_produtos)
produto_nome_entry.pack()

produto_quantidade_label = tk.Label(tela_produtos, text="Quantidade:")
produto_quantidade_label.pack()
produto_quantidade_entry = tk.Entry(tela_produtos)
produto_quantidade_entry.pack()

produto_marca_label = tk.Label(tela_produtos, text="Marca:")
produto_marca_label.pack()
produto_marca_entry = tk.Entry(tela_produtos)
produto_marca_entry.pack()

mensagem_produtos = tk.StringVar()
mensagem_produtos_label = tk.Label(tela_produtos, textvariable=mensagem_produtos)
mensagem_produtos_label.pack()

cadastrar_produto_button = tk.Button(tela_produtos, text="Cadastrar Produto", command=cadastrar_produto)
cadastrar_produto_button.pack()

editar_produto_button = tk.Button(tela_produtos, text="Editar Produto", command=editar_produto)
editar_produto_button.pack()

voltar_login_button_produtos = tk.Button(tela_produtos, text="Voltar para o Login", command=voltar_login_produtos)
voltar_login_button_produtos.pack()

window.mainloop()
