    # Exercício XII - Divisão Segura
    # Aluno: Paulo Donizete
    # Objetivo: Ler dois números e realizar a divisão do primeiro pelo segundo, caso o segundo seja diferente de 0.

    # inserção dos números

print("Insira o primeiro número aqui: ")
num1 = float(input())

print("Insira o segundo número aqui: ")
num2 = float(input())

    # verifica se o segundo número é diferente de 0, habilitando a operação.

if num2 == 0:
    print("Divisão invalida.")
else:
    resultado = num1 / num2
    print(f"O resultado é: {resultado:.2f}")