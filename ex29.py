    # Exercício XXIX — O maior de três
    # Aluno: Paulo Donizete
    # Objetivo: ler três números diferentes e determinar qual deles é o maior

    # inserção dos números

print("Insira o primeiro número aqui: ")
num1 = float(input())

print("Insira o segundo número aqui: ")
num2 = float(input())

print("Insira o terceiro número aqui: ")
num3 = float(input())

    # verificação de qual número é maior

if num1 > num2 and num1 > num3:
    print(f"O maior é {num1:.1f}")
elif num2 > num1 and num2 > num3:
    print(f"O maior é {num2:.1f}")
else:
    print(f"O maior é {num3:.1f}")