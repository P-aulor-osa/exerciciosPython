    # Exercício XXXVIII — Equação do 2º grau
    # Aluno: Paulo Donizete
    # Objetivo: calcular as raízes de uma equação do segundo grau usando os coeficientes a, b e c.

    # inserção dos coeficientes

print("Insira o primeiro coeficiente aqui: ")
a = float(input())

print("Insira o segundo coeficiente aqui: ")
b = float(input())

print("Insira o terceiro coeficiente aqui: ")
c = float(input())

    # verificação 1: valida se 'a' é zero

if a == 0.0:
    print("Não é uma equação do 2° grau.")

else:

    # calcula o delta

    delta = (b ** 2.0) - (4.0 * a * c)

    # verificação 2: avalia ar raízes reais baseadas em delta

if delta < 0.0:
    print("Não existem raízes reais.")
elif delta == 0.0:
    x = - b / (2.0 * a)
    print(f"Uma raiz: x = {x}")
else:
    x1 = (-b + (delta ** 0.5)) / (2.0 * a)
    x2 = (-b + (delta ** 0.5)) / (2.0 * a)
    print(f"x1 = {x1} e x2 = {x2}")