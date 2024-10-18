# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input("qual valor da sua hora? "))
mes = float(input("quantas horas vc trabalha por mês? "))
salarioBruto = mes * hora
IR = salarioBruto * (11 / 100)
INSS = salarioBruto * (8 / 100)
Sindicato = salarioBruto * (5 / 100)
descontos = IR + INSS + Sindicato
salarioLiq = salarioBruto - descontos

print("Salário Bruto: R$", salarioBruto,
"\nIR (11%): R$", IR,
"\nINSS (8%): R$", INSS,
"\nSindicato ( 5%): R$", Sindicato,
"\nSalário Liquido: R$", salarioLiq)
