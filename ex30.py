    # Exercício XXX — Ano bissexto
    # Aluno: Paulo Donizete
    # Objetivo: verificar se um ano informado é bissexto seguindo as regras oficiais.

    # inserção do ano

print("Insira o ano que deseja verificar aqui: ")
ano = int(input())

    # verifica o ano inserido e aplica a regra do ano bissexto

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto.")
else:
    print("Ano regular")