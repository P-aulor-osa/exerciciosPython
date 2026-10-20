    # Exercício XXXIV — Aprovação com frequência
    # Aluno: Paulo Donizete
    # Objetivo: verificar a aprovação considerando notas (média >= 7.0) e frequência (>= 75%).

    # inserção das notas e frequência

print("Insira a primeira nota aqui: ")
nota1 = float(input())

print("Insira a segunda nota aqui: ")
nota2 = float(input())

print("Insira a terceira nota aqui: ")
nota3 = float(input())

print("Insira a porcentagem da frequência do aluno aqui: ")
freq = float(input())

    # cálculo da média

media = (nota1 + nota2 + nota3) / 3

    # verifica a média e a frequência, aprovando ou reprovando de acordo com os valores


if media < 7.0 and freq < 75:
    print("Reprovado por falta e notas. Melhore!")
elif freq < 75:
    print("Reprovado por falta.")
elif media < 7.0:
    print("Reprovado por nota.")
else: 
    print("Aprovado!")