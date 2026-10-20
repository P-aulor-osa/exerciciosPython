    # Exercício XVI - Saque no Caixa Eletrônico
    # Aluno: Paulo Donizete
    # Objetivo: Verificar se o saldo é maior que a quantidade a sacar desejada, e apresentar o novo saldo.

    # inserção do saldo e do valor a sacar

print("Insira o saldo atual aqui: ")
saldo = float(input())

print("Insira o valor a sacar aqui: ")
saque = float(input())  

if saldo < saque:
    print("Saldo insuficente.")
else: 
    resto = saldo - saque
    print(f"Saque realizado. O novo saldo é R${resto:.2f50}")