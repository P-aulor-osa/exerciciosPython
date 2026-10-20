
    # Exercício XV - Desconto na Compra
    # Aluno: Paulo Donizete
    # Objetivo: Verificar o preço de uma compra, emitindo um desconto de 10% caso passe de R$100,00

    # inserção do valor da compra

print("Insira o preço total da compra aqui: ")
preco = float(input())

     # verifica se o preço é maior que R$100,00, e mostra o resultado apropriado

if preco < 100:
    print(f"O valor final é R${preco:.2f}")
else:
    desc = preco * 0.10
    total = preco - desc
    print(f"O valor final é R${total:.2f}")