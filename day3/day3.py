from tkinter import Tk, Frame, Label, Entry, Button, StringVar
from tkinter.messagebox import showerror, showinfo
import pandas as pd

# Criar a janela principal do aplicativo
app = Tk()
app.title("Cadastro de Usuários")

# Configurar o tema dark com azul
app.configure(bg='#1a1a1a')


# Criar um DataFrame vazio para armazenar os usuários
df_usuario = pd.DataFrame(columns=['nome', 'email', 'senha'])

# Criar um frame para o formulário de cadastro
form_frame = Frame(app, bg='#1a1a1a')
form_frame.pack(pady=20)

# Criar os widgets do formulário
nome_label = Label(form_frame, text="Nome:", bg='#1a1a1a', fg='#bbbbbb')
nome_label.grid(row=0, column=0)
nome_entry = Entry(form_frame, bg='#3a3a3a', fg='#bbbbbb')
nome_entry.grid(row=0, column=1)

email_label = Label(form_frame, text="Email:", bg='#1a1a1a', fg='#bbbbbb')
email_label.grid(row=1, column=0)
email_entry = Entry(form_frame, bg='#3a3a3a', fg='#bbbbbb')
email_entry.grid(row=1, column=1)

senha_label = Label(form_frame, text="Senha:", bg='#1a1a1a', fg='#bbbbbb')
senha_label.grid(row=2, column=0)
senha_entry = Entry(form_frame, bg='#3a3a3a', fg='#bbbbbb', show="*")
senha_entry.grid(row=2, column=1)

senha_conf_label = Label(form_frame, text="Confirmar Senha:", bg='#1a1a1a', fg='#bbbbbb')
senha_conf_label.grid(row=3, column=0)
senha_conf_entry = Entry(form_frame, bg='#3a3a3a', fg='#bbbbbb', show="*")
senha_conf_entry.grid(row=3, column=1)

# Criar uma função para cadastrar um usuário
def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()
    senha_conf = senha_conf_entry.get()

    if senha != senha_conf:
        showerror("Erro", "As senhas não são iguais")
        return

    if email in df_usuario['email'].values:
        showerror("Erro", "Esse email já foi utilizado")
        return

    df_usuario.loc[len(df_usuario)] = [nome, email, senha]
    showinfo("Sucesso", "Usuário cadastrado com sucesso")
    limpar_campos()

# Criar uma função para limpar os campos do formulário
def limpar_campos():
    nome_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    senha_entry.delete(0, 'end')
    senha_conf_entry.delete(0, 'end')

# Criar um botão para cadastrar um usuário
cadastrar_button = Button(form_frame, text="Cadastrar", command=cadastrar_usuario, bg='#4aa6ff', fg='#ffffff')
cadastrar_button.grid(row=4, columnspan=2, pady=10)

# Criar um frame para a área de pesquisa
search_frame = Frame(app, bg='#1a1a1a')
search_frame.pack(pady=20)

# Criar os widgets da área de pesquisa
search_label = Label(search_frame, text="Pesquisar por nome ou email:", bg='#1a1a1a', fg='#bbbbbb')
search_label.grid(row=0, column=0, columnspan=2)
search_entry = Entry(search_frame, bg='#3a3a3a', fg='#bbbbbb')
search_entry.grid(row=1, column=0, columnspan=2, pady=(10, 0))

# Criar uma função para pesquisar um usuário
def pesquisar_usuario():
    query = search_entry.get().lower()
    results = df_usuario[(df_usuario['nome'].str.lower().str.contains(query)) | (df_usuario['email'].str.lower().str.contains(query))]
    if len(results) == 0:
        showinfo("Nenhum resultado", "Nenhum usuário foi encontrado com essa consulta.")
    else:
        result_label.config(text=results.to_string(index=False))

# Criar um botão para pesquisar um usuário
pesquisar_button = Button(search_frame, text="Pesquisar", command=pesquisar_usuario, bg='#4aa6ff', fg='#ffffff')
pesquisar_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# Criar uma label para exibir os resultados da pesquisa
result_label = Label(search_frame, text="", bg='#3a3a3a', fg='#bbbbbb')
result_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Criar uma função para listar todos os usuários cadastrados
def listar_usuarios():
    if len(df_usuario) == 0:
        showinfo("Nenhum usuário", "Nenhum usuário foi cadastrado.")
    else:
        result_label.config(text=df_usuario.to_string(index=False))

# Criar um botão para listar todos os usuários cadastrados
listar_button = Button(search_frame, text="Listar usuários", command=listar_usuarios, bg='#4aa6ff', fg='#ffffff')
listar_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Iniciar o loop principal do aplicativo
app.mainloop()