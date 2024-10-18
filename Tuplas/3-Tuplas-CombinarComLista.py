# 3. Operações com tuplas: Crie duas tuplas: uma com nomes de frutas e outra com suas respectivas cores. Combine-as para formar uma lista de pares de frutas e cores.
frutas = ('morango', 'limão', 'banana')
cores = ('vermelho', 'verde', 'amarelo')
frutasCores = list(zip(frutas, cores))
print(frutasCores)