import os
# "def limpar tela", tem como função limpar o terminal  a cada opção do usuário. Para utilizar esse comando precisei importar a biblioteca "os".
def limpar_tela():
    os.system("cls")
# utilizei o método "def menu_principal" para o usuário poder voltar ao menu, quando ele termina a execução da funcionalidade.
def menu_principal():
    limpar_tela()
    print("Bem-Vindo ao MetrôBot \n")
    print("1. Cadastrar usuário")
    print("2. Tirar dúvidas")
    print("3. Mapa da estação")
    print("4. Encerrar\n")

    escolha_usuário = input("Qual das opções, você precisa ? ")
    
    if escolha_usuário == "1":
        cadastrar_usuario()
    elif escolha_usuário == "2":
        tirar_duvidas()
    elif escolha_usuário == "3":
        mapa_estacao()
    elif escolha_usuário == "4":
        print("Encerrando o programa.")
    else:
        print("Opção inválida!")
        menu_principal()
    
    
def cadastrar_usuario():
    limpar_tela()
    tentativas = 0
    max_tentativas = 3
    #enquanto a tentativa do usuário for menor que 3,o sistema ira permitir ele tentar escrever o email novamente ,caso erre 
    while tentativas < max_tentativas:
        email_usuário = input("Insira o email:")
        email_correto = input(f"O email está correto {email_usuário} ? (S/N) ")
        #o .lower ira registar a resposta do usuário em minusculo , desse modo n necessito colocar email_correto == s or email_correto == S
        if email_correto.lower():
            print("Email cadastrado com sucesso.")
            break
        else:
            tentativas += 1 
            print("Tente novamente, por gentileza.")
    if tentativas == max_tentativas:
            print("Número máximo de tentativas para o email atingido. Retornando ao Menu principal.")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            
        
    tentativas = 0 
    while tentativas < max_tentativas:         
        senha_usuário = input("Insira a senha: ")
        senha_correto = input(f"A senha está correto {senha_usuário} ? (S/N)")
        #Coloquei o "lower" para que o sistema consiga ler "S" maiusuculo e o "s" minusculo ,sem a necessidade de fazer o "or".
        if senha_correto.lower() == "s":
            print("Senha cadastrado com sucesso.") 
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            break
        else:
            tentativas += 1 
            print("Tente novamente, por gentileza.")
            
    if tentativas == max_tentativas:
        print("Número máximo de tentativas para a senha atingido.")
        input("Pressione Enter para retornar ao menu.")
        menu_principal()
        
def tirar_duvidas():
    limpar_tela()
    duvida_usuário = input("Qual seria sua dúvida ? ")
    print("Dúvida resgistrada.")
    input("Pressione Enter para retornar ao menu.")
    menu_principal()
    
def mapa_estacao():
    limpar_tela()
    print("Mapa da estação.")
    input("Pressione Enter para retornar ao menu.")
    menu_principal()
    
menu_principal()



    

    

