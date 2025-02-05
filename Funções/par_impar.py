# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def par_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

if __name__ == '__main__':
    numero = int(input("Digite um número inteiro: "))
    resultado = par_impar(numero)
    print(f"O número {numero} é {resultado}.")
