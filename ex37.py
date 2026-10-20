    # Exercício XXXVII — Três números em ordem crescente
    # Aluno: Paulo Donizete
    # Objetivo: ler três números diferentes e exibi-los em ordem crescente usando condicionais.

    # inserção dos valores

print("Insira o primeiro número aqui: ")
num1 = float(input())

print("Insira o segundo número aqui: ")
num2 = float(input())

print("Insira o terceiro número aqui: ")
num3 = float(input())

    # verifica todas as ordens possíveis para ordenação manual

if num1 <= num2 and num2 <= num3:
    print(f"Crescente: {num1:.2f} {num2:.2f} {num3:.2f}")
elif num1 <= num3 and num3 <= num2:
    print(f"Crescente: {num1:.2f} {num3:.2f} {num2:.2f}")
elif num2 <= num1 and num1 <= num3:
    print(f"Crescente: {num2:.2f} {num1:.2f} {num3:.2f}")
elif num2 <= num3 and num3 <= num1:
    print(f"Crescente: {num2:.2f} {num3:.2f} {num1:.2f}")
elif num3 <= num1 and num1 <= num2:
    print(f"Crescente: {num3:.2f} {num1:.2f} {num2:.2f}")
else:
    print(f"Crescente: {num3:.2f} {num2:.2f} {num1:.2f}")