    # Exercício XXXVI — Pedra, papel e tesoura
    # Aluno: Paulo Donizete
    # Objetivo: simular o jogo jokenpô entre dois jogadores e determinar o vencedor.

    #jogadas efetuadas por ambos os jogaores

print("Jogador 1: pedra, papel ou tesoura")
player1 = input()

print("Jogador 2: pedra, papel ou tesoura")
player2 = input()

    #verifica as jogadas e determina o resultado apropriado

if (player1 not in "pedra" "papel" "tesoura") or (player2 not in "pedra" "papel" "tesoura"):
    print("Jogada inválida, trapaceiro!")
elif player1 == player2:
    print("Empate.")
elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "tesoura" and player2 == "papel") or (player1 == "papel" and player2 == "pedra"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")    