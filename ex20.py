    # Exercício XX - Dia da Semana
    # Aluno: Paulo Donizete
    # Objetivo: Ler um número de 1 a 7, e apresentar o dia da semana correspondente

    # inserção de número

print("Insira um número de 1 a 7 aqui: ")
diaSmn = int(input())

    # verificação, cada número de 1 a 7 puxa um dia diferente, invalidando números acima de 7

if(diaSmn == 1):
  print("Domingo.")
  
elif(diaSmn == 2):
    print("Segunda-feira.")
  
elif(diaSmn == 3):
    print("Terça-feira.")
  
elif(diaSmn == 4):
    print("Quarta-feira.")
  
elif(diaSmn == 5):
    print("Quinta-feira.")
  
elif(diaSmn == 6):
    print("Sexta-feira.")
  
elif(diaSmn == 7):
    print("Sábado.")
else:
    print("Data inválida.")
