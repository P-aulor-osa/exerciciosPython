    # Exercício XIV - Radar de Velocidade
    # Aluno: Paulo Donizete
    # Objetivo: Verificar a velocidade de um carro, mostrando um aviso caso ele passar do limite de 80km/h.

    # inserção da velocidade

print("Insira a velocidade do carro aqui: ")
velo = float(input())

    # verifica se a velocidade estava acima de 80 e mostra o resultado apropriado.

if velo > 80:
    print(f"Multado! Você ultrapassou {velo - 80:.1f}km/h do limite.")
else:
    print("Velocidade dentro do limite. Bon Voyage!")