from data_pre_processing import data_pre_processing, divide_dataframe

data = data_pre_processing("Dados_estatisticos_avioes.csv")

metade = int(data.shape[0] / 2)

treino = data[:metade]
teste = data[metade:]

treino_x, treino_y = divide_dataframe(treino)

teste_x, teste_y = divide_dataframe(teste)

print(treino_x)
