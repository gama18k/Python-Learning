# 5. Listas dentro de listas: Crie uma lista que contenha 3 sublistas, cada uma representando as notas de um aluno em 3 provas. Calcule a média de notas de cada aluno.

notas_alunos = [
    [8.5, 9.0, 7.5],  
    [6.0, 7.0, 5.5],  
    [9.5, 10.0, 9.0] 
]

medias = []

for notas in notas_alunos:
    soma = 0  
    for nota in notas:
        soma += nota  
    media = soma / len(notas)
    medias.append(media) 


for i in range(len(medias)):
    print(f"Média do aluno {i + 1}: {medias[i]:.2f}")