# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input("digite a data:")
dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

# quantos dias tem cada mês
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
# veririca se é ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # fevereiro tem 29 dias em anos bissextos
    meses[1] = 29

# verifique se o mês é válido e se o dia é válido para esse mês
if mes >= 1 and mes <= 12:
    if dia >= 1 and dia <= meses[mes - 1]:
        print("data válida")
    else:
        print("data inválida")
else:
    print("data inválida")
