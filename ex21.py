    # Exercício XXI - Faixa Etária
    # Aluno: Paulo Donizete
    # Objetivo: Ler a idade do usuário e apresentar a faixa etária adequada.

    # inserção da idade

print("Insira sua idade aqui: ")
idade = int(input())

    # verifica a idade, mostrando a faixa etária de acordo com o valor ninserido.

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")