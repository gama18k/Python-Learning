# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoArquivo = float(input("tamanho do arquivo para download (em MB): "))
velocidadeNet = float(input("velocidade do link de Internet (em Mbps): "))

# (1 Mbps = 0.125 MBps)
velocidadeNetMBps = velocidadeNet * 0.125

downloadSegs = tamanhoArquivo / velocidadeNetMBps
downloadMins = downloadSegs / 60
print(f"O tempo aproximado de download é de {downloadMins:.2f} minutos.")
