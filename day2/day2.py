import pandas as pd
df_usuario={
    'nome':[],
    'email':[],
    'senha':[]
}
df_usuario = pd.DataFrame(df_usuario)

txt_alt=""" O que você deseja alterar?
1 - Nome
2 - email
3 - senha
"""

def cad_u():
    nome = input('Digite o seu nome:')
    email = input('Digite o seu email:')
    senha = input('Digite o sua senha:')
    senha_conf = input('Confirme a sua senha:')
    
    while email in df_usuario['email'].values:
        print('Esse email já foi ultilizado tente outro')
        email = input('Digite o seu email:')
    
    while senha != senha_conf:
        print('As senhas não são iguais, tente novamente')
        senha = input('Digite o sua senha:')
        senha_conf = input('Confirme a sua senha:')
        
    tamanho_df=len(df_usuario)
    df_usuario.loc[tamanho_df]=''
    df_usuario.iloc[tamanho_df,0]=nome
    df_usuario.iloc[tamanho_df,1]=email
    df_usuario.iloc[tamanho_df,2]=senha

def pesquisa(pesquisa):
    if pesquisa in df_usuario['email'].values:
        print(df_usuario[df_usuario["email"]==pesquisa])
    elif pesquisa in df_usuario['nome'].values:
        print(df_usuario[df_usuario["nome"]==pesquisa])
    else:
        print('Não temos esse usuario na base de dados')

def atualizar(pesquisa):
    if pesquisa in df_usuario['email'].values:
        email=pesquisa
        alteracao=input(txt_alt)
        
        if alteracao=='1':
            df_alterado=df_usuario[df_usuario["email"]==email]
            
            df_alterado['nome']=input("Novo nome: ")

            df_usuario[df_usuario["email"]==email]=df_alterado

        elif alteracao=='2':

            df_alterado=df_usuario[df_usuario["email"]==email]

            nv_email=input("Novo email: ")
            while nv_email in df_usuario['email'].values:
                print('Esse email já foi ultilizado tente outro')
                nv_email = input('Digite outro email:')

            df_alterado['email']= nv_email
            df_usuario[df_usuario["email"]==email]=df_alterado


        elif alteracao=='3':
            df_alterado=df_usuario[df_usuario["email"]==email]
            df_alterado['senha']=input("Nova senha: ")
            df_usuario[df_usuario["email"]==email]=df_alterado
    elif pesquisa in df_usuario['nome'].values:
        nome=pesquisa
        alteracao=input(txt_alt)
        if alteracao=='1':
            df_alterado=df_usuario[df_usuario["nome"]==nome]
            df_alterado['nome']=input("Novo nome: ")
            df_usuario[df_usuario["nome"]==nome]=df_alterado
        elif alteracao=='2':
            df_alterado=df_usuario[df_usuario["nome"]==nome]
            nv_email=input("Novo email: ")
            while nv_email in df_usuario['email'].values:
                print('Esse email já foi ultilizado tente outro')
                nv_email = input('Digite outro email:')
            df_alterado['email']= nv_email
            df_usuario[df_usuario["nome"]==nome]=df_alterado
        elif alteracao=='3':
            df_alterado=df_usuario[df_usuario["nome"]==nome]
            df_alterado['senha']=input("Nova senha: ")
            df_usuario[df_usuario["nome"]==nome]=df_alterado
    else:
        print('Não temos esse usuario na base de dados')

def main():
    acao=input("""
Bem vindo ao nosso sistema de cadastros:
Qual ação você deseja ultilizar?
        1 - Cadastrar novo usuario?
        2 - Fazer a consulta de um usuario?
        3 - Atualizar o dado de algum usuario
        4 - Listar todos os usuarios
        5 - Fechar a interaface
""")
    while acao not in ['1', '2', '3','4','5']:
        print("Opão invalida, tente novamente")
        acao=input("""
Bem vindo ao nosso sistema de cadastros:
Qual ação você deseja ultilizar?
        1 - Cadastrar novo usuario?
        2 - Fazer uma pesquisa de um novo usuario?
        3 - Atualizar o dado de algum usuario
        4 - Fechar a interaface
""")
    if acao == "1":
        cad_u()
        main()
    elif acao =='2':
        v_pesq=input('Digite o nome ou o email do usuario que deseja pesquisar')
        pesquisa(v_pesq)
        main()
    elif acao == '3':
        v_atua=input('Digite o nome ou o email do usuario que deseja atualizar as informações')
        atualizar(v_atua)
        main()
    elif acao == '4':
        print(df_usuario)
        main()
    elif acao == "5":
        print('Fechando a interface')
main()

