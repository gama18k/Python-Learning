# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = float(input("digite o valor de A: "))
if a == 0:
    print("A não pode ser zero")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = b**2 - 4 * a * c
    print(f"O valor de delta é: {delta}")

if (delta<0):
    print("não tem raizes reais")
elif delta==0:
    raiz = -b / (2 * a)
    print(f"a equação possui apenas uma raiz real: {raiz}")
else:
    raiz_quadrada_delta = delta ** 0.5
    raiz1 = (-b + raiz_quadrada_delta) / (2 * a)
    raiz2 = (-b - raiz_quadrada_delta) / (2 * a)
    print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
