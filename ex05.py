    # Exercício V - Minutos para Horas  
    #  Aluno: Paulo Donizete
    #  Objetivo: Ler uma quantidade de minutos e apresentar a mesma em um formato de horas e minutos

    # inserção do tempo em minutos

print("Insira o tempo em minutos aqui: ")
minutos = int(input())

    # operação de conversão

horas = minutos // 60
resto = minutos % 60

    # resultado
print(f"{minutos} minutos equivalem a {horas} hora(s) e {resto} minutos.")