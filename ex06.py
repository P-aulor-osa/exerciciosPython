    # Exercício VI - Compra na Cantina
    # Aluno: Paulo Donizete
    # Objetivo: Ler o preço, quantidade e valor pago pelo cliente, mostrar o valor pago e o troco.

    # inserção do valor do produto, quantidade e valor pago

print("Insira o preço do produto aqui: ")
preco = float(input())

print("Insira a quantidade do produto aqui: ")
quant = int(input())

print("Insira o valor pago aqui: ")
valPago = float(input())

    # cálculo do valor total e troco

total = preco * quant
troco = valPago - total

    # resultado

print(f"Total: R${total:.2f}")
print(f"Troco: R${troco}")