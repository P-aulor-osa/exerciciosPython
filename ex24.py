    # Exercício XXIV — Calculadora de IMC
    # Aluno: Paulo Donizete
    # Objetivo: calcular o IMC com base no peso e altura, exibindo a classificação.

    # inserção do peso e altura

print("Insira seu peso em kg aqui: ")
peso = float(input())

print("Insira sua altura em metros aqui: ")
altura = float(input())

    # cálculo do IMC

imc = peso / (altura * altura)

    # verificação da classificação do IMC

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso.")  
elif imc < 25:
    print(f"IMC: {imc:.2f} - Peso normal.")
elif imc < 30:
    print(f"IMC: {imc:.2f} - Sobrepeso.")
else:
    print(f"IMC: {imc:.2f} - Obesidade.")