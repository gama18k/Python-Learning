# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto e 3% para o Sindicato. O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
#         (-) INSS ( 10%)
#         Sindicato (3%)                    

valorHora = float(input("digite o valor da sua hora:" ))
horasTrabalhadas = float(input("digite quantas horas trabalhou: "))

salarioBruto = valorHora * horasTrabalhadas
percentualIR = 0

if salarioBruto <= 900:
     percentualIR = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
     percentualIR = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
     percentualIR = 10
else:
     percentualIR = 20

valorIR = salarioBruto * (percentualIR / 100)
valorINSS = salarioBruto * 0.1
valorSindicato = salarioBruto * 0.03
descontosTotais = salarioBruto - valorIR - valorINSS - valorSindicato
salarioLiquido = salarioBruto - descontosTotais

print(f"salário bruto: R$ {salarioBruto:.2f}")
print(f"valor IR: R$ {valorIR:.2f}")
print(f"valor INSS: R$ {valorINSS:.2f}")
print(f"valor sindicato: R$ {valorSindicato:.2f}")
print(f"descontos totais: R$ {descontosTotais:.2f}")
print(f"salário líquido: R$ {salarioLiquido:.2f}")
