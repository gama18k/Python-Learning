# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("qual sua altura? "))
genero = input("você é F ou M? ").strip().upper()
pesoIdealM = (72.7* altura) - 58
pesoIdealF = (62.1* altura) - 44.7

if genero == 'F':
    print("seu peso ideal é ", "{:.2f}".format(pesoIdealF))

if genero == 'M':
    print("seu peso ideal é ", "{:.2f}".format(pesoIdealM))

else:
    print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
