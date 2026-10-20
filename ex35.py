    # Exercício XXXV — Calculadora
    # Aluno: Paulo Donizete
    # Objetivo: realizar operações matemáticas básicas (+, -, *, /) com tratamento de erros.

    # inserção dos valores para cálculo e operador

print("Insira o primeiro número aqui: ")
num1 = float(input())

print("Insira o segundo número aqui: ")
num2 = float(input())

print("Insira o operador aqui: ")
op = input()

    # verifica se o operador é valido, qual operação deve ser efetuada, e restringe divisão por zero

if op not in "+" "-" "*" "/":
    print("Operador inválido")

if op == "+":
    conta = num1 + num2
    print(f"Resultado: {conta:.2f}")
elif op == "-":
    conta = num1 - num2
    print(f"Resultado: {conta:.2f}")
elif op == "*":
    conta = num1 * num2
    print(f"Resultado: {conta:.2f}")
elif op == "/":
    if num2 == 0:
        print("Erro: divisão por zero.")
    else:
        conta = num1 / num2
        print(f"Resultado: {conta:.2f}")