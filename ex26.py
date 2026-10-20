    # Exercício XXVI — Desconto progressivo
    # Aluno: Paulo Donizete
    # Objetivo: calcular o valor do desconto progressivo e o valor final da compra.

    # inserção do valor da compra

print("Insira o valor da compra aqui: ")
valor = float(input())

    # cálculo do desconto progressivo e do valor final da compra

if valor < 50.0:
    desc_percent = 0.0
elif valor < 100.0:
    desc_percent = 0.05
elif valor < 200.0:
    desc_percent =  0.10
else:
    desc_percent = 0.15

desc = valor * desc_percent
valor_fin = valor - desc

    # resultado

print(f"Desconto aplicado: R${desc:.2f}")
print(f"Valor final da compra: R${valor_fin:.2f}")