# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

def tipoNumero(numero):
    if round(numero) == numero:
        return f"o {numero:.2f} é inteiro"
    else:
        return f"o {numero:.2f} é decimal"
    
numero = float(input("digite um número:"))
resultado = tipoNumero(numero)
print(resultado)
