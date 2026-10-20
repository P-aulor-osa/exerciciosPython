    #    # Exercício XL — Bilheteria da Festa do Pinhão
    # Aluno: Paulo Donizete
    # Objetivo: simular a venda de ingressos calculando descontos, formas de pagamento e gratuidade.

    # inserção da idade, e se o usuário é estudante 
    
print("Insira sua idade aqui: ")
idade = int(input())

print("Você é estudante? s/n")
estud = input()

    # encerra o programa se a resposta não for "sim" ou "não"

if estud not in "s" "sim" "n" "nao" "não":
    print("Resposta inválida")
    
    # verifica se a idade do usuário 6 ou menor, apresentando a mensagem adequada

if idade <= 6:
    print("Entrada gratuita. Divirta-se!")
    
    # verifica os requisitos para meia entrada, seja se o usuário tem entre 6 e 17, ou mais de 60 anos, ou se "sim" foi inserido na segunda entrada, se nenhum desses requisitos for atendido, paga entrada inteira
    
if (idade <= 17) or (idade >= 60) or (estud == "s" or "sim"):
    tipo_ticket = "Meia"
    valor_ini = 20.0
else:
    tipo_ticket = "Inteira"
    valor_ini = 40.0
    
    # inserção do método de pagamento
    
print("Insira o método de pagamento aqui: (1 = PIX, 2 = DÉBITO, 3 = CRÉDITO)")
pagam = int(input())

if pagam == 1:
    desc = "PIX"
    total = valor_ini - (valor_ini *0.05)
    print(f"Entrada: {tipo_ticket} Tipo de pagamento: {pagam} Valor total: {total}")
elif pagam == 2:
    desc = "Débito"
    total = valor_ini
    print(f"Entrada: {tipo_ticket} Tipo de pagamento: {pagam} Valor total: {total}")
elif pagam == 3:
    desc = "Crédito"
    total = valor_ini - (valor_ini *0.05)
    print(f"Entrada: {tipo_ticket} Tipo de pagamento: {pagam} Valor total: {total}")
else:
    print("Forma de pagamento inválida.")
    
