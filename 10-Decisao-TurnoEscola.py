# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = str(input("que turno você estuda? digite M para matutino, V para vespertino e N para noturno.\n")).upper()

if turno == "M":
     print("Bom Dia!")
elif turno == "V":
     print("Boa Tarde!")
else:
     print("Boa Noite!")
