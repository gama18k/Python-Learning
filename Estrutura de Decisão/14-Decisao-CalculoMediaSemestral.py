# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))

media = (nota1+nota2)/2

if media >= 9:
    print("nota 1:", nota1)
    print("nota 2:", nota2)
    print("média:", media)
    print("conceito: A")
    print("APROVADO")
elif media >= 7.5 and media < 9:
    print("nota 1:", nota1)
    print("nota 2:", nota2)
    print("média:", media)
    print("conceito: B")
    print("APROVADO")
elif media >= 6 and media < 7.5:
    print("nota 1:", nota1)
    print("nota 2:", nota2)
    print("média:", media)
    print("conceito: C")
    print("APROVADO")
elif media >= 4 and media < 6:
    print("nota 1:", nota1)
    print("nota 2:", nota2)
    print("média:", media)
    print("conceito: D")
    print("REPROVADO")
else:
    print("nota 1:", nota1)
    print("nota 2:", nota2)
    print("média:", media)
    print("conceito: E")
    print("REPROVADO")
