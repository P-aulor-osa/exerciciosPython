    #  Exercício III - Média de três notas
    #  Aluno: Paulo Donizete
    #  Objetivo: Extrair a média entre três valores de nota

    #  inserção das notas para efetuação do cálculo

print("Insira a primeira nota aqui: ")
nota1 = float(input())
print("Insira a segunda nota aqui: ")
nota2 = float(input())
print("Insira a terceira nota aqui: ")
nota3 = float(input())

    #  cálculo da média das notas

media = (nota1 + nota2 + nota3) / 3

    # resultado

print(f"A média extraída é: {media:.1f}")