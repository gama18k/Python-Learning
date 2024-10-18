# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input("número inteiro menor que 1000: "))

if numero < 0 or numero >= 1000:
    print("digite um número menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10

    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} centena" + ("s" if centenas > 1 else "")
    if dezenas > 0:
        if resultado:
            resultado += " e "
        resultado += f"{dezenas} dezena" + ("s" if dezenas > 1 else "")
    if unidades > 0:
        if resultado:
            resultado += " e "
        resultado += f"{unidades} unidade" + ("s" if unidades > 1 else "")
    
    print(resultado)
