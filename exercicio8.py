tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))

velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))


tempo_download = (tamanho_arquivo * 8) / (velocidade_internet * 60)

print("O tempo aproximado de download do arquivo é de", round(tempo_download, 2), "minutos.")
