    # Exercício XXXIX — Caixa eletrônico: contagem de notas
    # Aluno: Paulo Donizete
    # Objetivo: calcular a menor quantidade de notas de 100, 50, 20 e 10 para um determinado saque.

    # inserção do valor para saque

print("Insira o valor para saque. Use um valor que seja múltiplo de 10.")
saque = int(input())

    # verifica se o valor inserido é válido

if saque <= 0 or saque % 10 != 0:
    print("Valor inválido para saque.")

    # divisão inteira para notas e resto para os próximos valores

nota100 = saque // 100
resto = saque % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto / 10

    # resultado condicional exibindo apenas as notas utilizadas

resultado_str = ""
if nota100 > 0:
        resultado_str += f"{nota100} nota(s) de R$ 100  "
if nota50 > 0:
        resultado_str += f"{nota50} nota(s) de R$ 50  "
if nota20 > 0:
        resultado_str += f"{nota20} nota(s) de R$ 20  "
if nota10 > 0:
        resultado_str += f"{nota10} nota(s) de R$ 10"
print(resultado_str)