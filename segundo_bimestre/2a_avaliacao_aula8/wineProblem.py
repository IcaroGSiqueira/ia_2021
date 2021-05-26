import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import tree

arquivo = pd.read_csv('/home/icaro/Documents/2021.1/ia_2021/segundo_bimestre/2a_avaliacao_aula8/wine_dataset.csv')

print("\n", arquivo)
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)
print("\n", arquivo.head())

y = arquivo['style']
x = arquivo.drop('style', axis = 1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

print(x_treino.shape)
print(x_teste.shape)

modelo = ExtraTreesClassifier()
print("\n", modelo.fit(x_treino,y_treino))

modelo2 = tree.DecisionTreeClassifier()
print("\n",modelo2.fit(x_treino,y_treino))

resultados = modelo.score(x_teste, y_teste)
print("\nPrecisão Extra: ", resultados)

resultados2 = modelo2.score(x_teste, y_teste)
print("\nPrecisão Decision: ", resultados2)

#print("\nTeste: \n", x_teste[400:403], y_teste[400:403])
#previsoes = modelo.predict(x_teste[400:403])
#print("Acertos: ", previsoes)