    # Exercício XIX - Situação do Aluno
    # Aluno: Paulo Donizete
    # Objetivo: Ler duas notas, e de acordo com a média, apresentar se o aluno está aprovado, reprovado ou se requer recuperação.

    # inserção das notas

print("Insira a primeira nota aqui: ")
nota1 = float(input())

print("Insira a segunda nota aqui: ")
nota2 = float(input())

    # cálculo da média

media = (nota1 + nota2) / 2

    # verificação da situação do aluno

if media >= 7:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")