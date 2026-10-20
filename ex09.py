    #   Exercício IX - Par/Ímpar
    #   Aluno: Paulo Donizete
    #   Objetivo: Ler um número, e informar se é par ou ímpar.

    # inserção de número

print("Insira um número aqui: ")
num = int(input())

    # verificação se o resto da divisão do número por 2 é igual a 0, se sim, é par, caso contrário, é ímpar.

if num % 2 == 0:
    print("Par.")
else:
    print("Ímpar.")