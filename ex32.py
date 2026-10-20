    # Exercício XXXII — Login com usuário e senha
    # Aluno: Paulo Donizete
    # Objetivo: validar o usuário (aluno) e a senha (1234) usando decisões aninhadas.

    # inserção de usuário e senha


user = input("Insira o nome de usuário: ")

cod = input("Insira a senha: ")

    # decisão externa: verifica o nome do usuário
    
if user == "aluno": 
    
    # decisão interna: valida a senha
    
    while cod != "1234":
        print("Senha incorreta!")
        cod = input("Tente novamente:")     

    print("Login realizado com sucesso. Bem vindo(a)!")
    
else: 
    print("Usuário não encontrado.")