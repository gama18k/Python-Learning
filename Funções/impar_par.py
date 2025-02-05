# Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar
def par_impar(numero):
    return 'par' if numero % 2 == 0 else 'impar'

numero = int(input('Digite um número inteiro: '))
print(f"o {numero} é {par_impar(numero)}")
