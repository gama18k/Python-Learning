# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioUsuario = float(input("digite seu salário: "))
print("o salário antes do reajuste: ", salarioUsuario)
percentualAumento = 0
valorAumento = 0

if salarioUsuario <= 280:
     percentualAumento = 20 
elif salarioUsuario > 280 and salarioUsuario <= 700:
     percentualAumento = 15 
elif salarioUsuario > 700 and salarioUsuario <= 1500:
     percentualAumento = 10 
else:
     percentualAumento = 5

valorAumento = salarioUsuario * (percentualAumento / 100)
novoSalario = salarioUsuario + valorAumento

print(f"\nsalário antes do reajuste: R$ {salarioUsuario:.2f}")
print(f"Percentual de aumento aplicado: {percentualAumento}%")
print(f"Valor do aumento: R$ {valorAumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novoSalario:.2f}")
