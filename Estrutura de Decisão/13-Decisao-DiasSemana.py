# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
semana = {
     "1": "Domingo",
     "2": "Segunda-feira",
     "3": "Terça-feira",
     "4": "Quarta-feira",
     "5": "Quinta-feira",
     "6": "Sexta-feira",
     "7": "Sábado",
 }

inputUsuario = str(input("digite um número (1 a 7): "))

 if inputUsuario in semana:
     print(semana[inputUsuario])
else:
     print("número inválido")
