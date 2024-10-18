# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def defineTriangulo (lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3:
        return "isósceles"
    else:
        return "escaleno"

lado1 = int(input("digite o valor do primeiro lado: "))
lado2 = int(input("digite o valor do segundo lado: "))
lado3 = int(input("digite o valor do terceiro lado: "))

if (lado1+lado2>lado3) or (lado1+lado3>lado2) or (lado3+lado2>lado1):
    tipoTriangulo = defineTriangulo(lado1,lado2,lado3)
    print("os lados formam um triangulo " + tipoTriangulo)
else:
    print("não forma triangulo")
