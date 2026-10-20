    # Exercício XXIII — Cardápio da cantina
    # Aluno: Paulo Donizete
    # Objetivo: ler o código do produto e a quantidade, calculando o total a pagar.

    # apresentação do cardápio

print("=====   C A R D Á P I O   D A   C A N T I N A   =====")
print("Código  |   Produto   |  Preço")
print("   1    |  Pão de Q.  |  R$ 4,50")
print("   2    |   Coxinha   |  R$ 6,00")
print("   3    |   Pastel    |  R$ 7,00")
print("   4    |    Suco     |  R$ 5,00")
print("   5    |    Café     |  R$ 3,00")

    # inserção do código do produto e da quantidade

print("Insira o código do produto desejado: ")
cod = int(input())

    # verificação do código inserido, negando, ou calculando o total a pagar de acordo com o código e a quantidade inseridos.

if cod >= 6 or cod <= 0:
    print("Código inválido.")

elif cod == 1:
    print("Insira a quantidade desejada: ")
    quant = int(input())
    total = quant * 4.50
    print(f"Total: R$ {total:.2f}.")

elif cod == 2:
    print("Insira a quantidade desejada: ")
    quant = int(input())
    total = quant * 6.00
    print(f"Total: R$ {total:.2f}.")

elif cod == 3:
    print("Insira a quantidade desejada: ")
    quant = int(input())
    total = quant * 7.00
    print(f"Total: R$ {total:.2f}.")

elif cod == 4:
    print("Insira a quantidade desejada: ")
    quant = int(input())
    total = quant * 5.00
    print(f"Total: R$ {total:.2f}.")

elif cod == 5:
    print("Insira a quantidade desejada: ")
    quant = int(input())
    total = quant * 3.00
    print(f"Total: R$ {total:.2f}.")
