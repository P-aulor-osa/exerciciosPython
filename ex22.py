    # Exercício XXII — Termômetro da Serra
    # Aluno: Paulo Donizete
    # Objetivo: ler a temperatura em graus Celsius e mostrar a mensagem correspondente.

    # inserção da temperatura

print("Insira a temperatura em graus Celsius: ")
temp = float(input())

    # ve

if temp < 0:
    print("Abaixo de zero - Risco de geada!")
elif temp <10.0:
    print("Muito frio - Capriche no agasalho.")
elif temp < 18.0:
    print("Frio.")
elif temp < 25.0:
    print("Agradável.")
else:
    print("Calor.")