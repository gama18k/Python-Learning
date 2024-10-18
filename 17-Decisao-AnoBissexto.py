# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# Um ano é bissexto se for divisível por 4.
# No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.

def verificaAno(inputAno):
    if (inputAno % 4 == 0 and inputAno % 100 != 0) or (inputAno % 400 == 0):
        return True
    else:
        return False

inputAno = int(input("digite o ano: "))

if verificaAno(inputAno):
    print("ano bissexto")
else:
    print("ano normal")
