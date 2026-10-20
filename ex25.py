    # Exercício XXV — Radar com tipo de infração
    # Aluno: Paulo Donizete
    # Objetivo: calcular o percentual acima do limite e classificar o tipo de infração.

    # inserção da velocidade do veículo e do limite de velocidade

print("Insira a velocidade do veículo em km/h aqui: ")
velo = float(input())

print("Insira o limite de velocidade em km/h aqui: ")
limite = float(input())

if velo <= limite:
    print("Sem infração. Bon Voyage!")
else:
    # cálculo do percentual acima do limite
    percent = (velo - limite) / limite * 100

    # verificação do tipo de infração

    if percent <= 20:
        print(f"{percent:.2f}% acima do limite - Infração média.")
    elif percent <= 50:
        print(f"{percent:.2f}% acima do limite - Infração grave.")
    else:
        print(f"{percent:.2f}% acima do limite - Infração gravíssima.")