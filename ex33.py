    # Exercício XXXIII — Voto obrigatório
    # Aluno: Paulo Donizete
    # Objetivo: informar a situação eleitoral de uma pessoa com base na idade.

    # inserção da iddade

print("Insira sua idade aqui: ")
idade = int(input())

    # verifica o valor inserido e apresenta a mensagem apropriada

if idade < 16:
    print("Não pode votar.")
elif idade <= 18:
    print("Voto facultativo.")
elif idade <= 69:
    print("Voto obrigatório.")
elif idade >= 70:
    print("Voto facultativo.")