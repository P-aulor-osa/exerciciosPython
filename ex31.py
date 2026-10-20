    # Exercício XXXI — Tipo de triângulo
    # Aluno: Paulo Donizete
    # Objetivo: ler os lados de um triângulo, validar a formação e classificá-lo.

    # inserção dos três ângulos

print("Insira a medida do primeiro lado aqui: ")
l1 = float(input())

print("Insira a medida do segundo lado aqui: ")
l2 = float(input())

print("Insira a medida do terceiro lado aqui: ")
l3 = float(input())

    # verifica a regra de existência do triângulo

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

    # classifica o triângulo

    if l1 == l2 and l2 == l3:
        print("Equilátero.")
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print("Isósceles.")
    else:
        print("Escaleno.")
    
else: 
    print("Esses lados não formam um triângulo.")