# 4. Iteração sobre dicionários: Crie um dicionário com três palavras e seus significados. Imprima cada palavra e seu significado usando um loop.
dict = {'water': 'agua',
            'fire': 'fogo',
            'earth': 'terra'}
for palavra, significado in dict.items():
    print(f"{palavra}: {significado}")