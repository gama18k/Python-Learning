# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

def calculoMedia (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

calculoMedia(nota1,nota2,nota3)


# outra forma de fazer:
# nota1 = float(input("digite a primeira nota: "))
# nota2 = float(input("digite a segunda nota: "))
# nota3 = float(input("digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# if media == 10:
#     print("Aprovado com Distinção")
# elif media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")
