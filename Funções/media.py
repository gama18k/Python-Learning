# Desenvolva um programa que leia quatro notas e que apresente a média final

def calc_media():
    notas = [float(input(f"digite a {i+1}ª nota: ")) for i in range(4)]
    media = sum(notas) / len(notas)
    print(f"a média final é: {media:.2f}")

if __name__ == '__main__':
    calc_media()
