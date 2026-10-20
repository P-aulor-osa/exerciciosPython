    # Exercício X - Aprovado/Reprovado
    # Aluno: Paulo Donizete
    # Objetivo: Ler duas notas, e de acordo com a média, apresentar se o aluno está aprovado ou reprovado.

    # inserção das notas

print("Insira a primeira nota aqui: ")
nota1 = float(input())

print("Insira a segunda nota aqui: ")
nota2 = float(input())

    # cálculo da média das notas

media = (nota1 + nota2) / 2

    # verificação se a média é maior ou igual a 7, mostrando o resultado apropriado.

if media >= 7:
    print(f"A média do aluno é: {media:.1f}. Aprovado!")
else: 
    print(f"A média do aluno é: {media:.1f}. Reprovado.")