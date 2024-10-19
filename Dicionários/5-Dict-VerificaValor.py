# 5. Verificar existência de chave: Crie um dicionário com 5 estados brasileiros e suas capitais. Verifique se "São Paulo" está no dicionário e imprima a capital correspondente.

brasil = {'são paulo': 'sp',
          'rio de janeiro': 'rj',
          'minas gerais': 'mg',
          'espirito santo': 'es',
          'santa catarina': 'sc'}

if 'são paulo' in brasil:
    capital = brasil['são paulo']
    print(f"a capital de são paulo é: {capital}")
else:
    print("estado não encontrado.")
