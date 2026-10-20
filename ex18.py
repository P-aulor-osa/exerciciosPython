    
  # Exercício XVIII - Maior de Dois ou Igual
  # Aluno: Paulo Donizete
  # Objetivo: Ler dois números e informar qual é o maior ou se são iguais.

  # inserção dos números

print("Insira o primeiro número aqui: ")
num1 = float(input())

print("Insira o segundo número aqui: ")
num2 = float(input())

    # verificação de qual número é maior ou se são iguais

if num1 == num2:
    print("Ambos são iguais.")
elif num1 > num2:
    print(f"O maior é {num1:.2f}")
else:
    print(f"O maior é {num2:.2f}")