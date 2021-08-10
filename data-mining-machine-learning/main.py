from data_pre_processing import data_pre_processing, divide_dataframe
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import sklearn.metrics as metrics
from sklearn.neighbors import NearestNeighbors
from sklearn import tree

data = data_pre_processing("Dados_estatisticos_avioes.csv")

metade = int(data.shape[0] / 2)

treino = data[:metade]
teste = data[metade:]

treino_x, treino_y = divide_dataframe(treino)

teste_x, teste_y = divide_dataframe(teste)

escala = MinMaxScaler(feature_range = (0,1))
teste_x = escala.fit_transform(teste_x)
treino_x = escala.fit_transform(treino_x)


print("MLP")

clf = MLPClassifier(hidden_layer_sizes = (8,4,2), max_iter = 100,
                                solver = "sgd", verbose = 0, tol = 1e-8, random_state = 777,
                                learning_rate_init = .05, learning_rate = "adaptive", activation = "tanh")

clf.fit(treino_x, treino_y)
y_result = clf.predict(teste_x)


print(confusion_matrix(teste_y, y_result))
print()
print("--------------------------------------------------------------------------------")
print()
print(classification_report(teste_y, y_result))

print("KNN")

nkk = NearestNeighbors(n_neighbors=3)
nkk.fit(treino_x, treino_y)
y_result = nkk.kneighbors(teste_x)


print(confusion_matrix(teste_y, y_result))
print()
print("--------------------------------------------------------------------------------")
print()
print(classification_report(teste_y, y_result))

print("Decision Tree")

arvore = tree.DecisionTreeClassifier()
arvore.fit(treino_x, treino_y)
y_result = arvore.predict(teste_x)

print(confusion_matrix(teste_y, y_result))
print()
print("--------------------------------------------------------------------------------")
print()
print(classification_report(teste_y, y_result))

