# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("qual sua altura? "))
pesoIdeal = (72.7* altura) - 58
print("seu peso ideal é ", "{:.2f}".format(pesoIdeal))
