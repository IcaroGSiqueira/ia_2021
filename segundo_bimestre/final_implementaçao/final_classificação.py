#Importação das bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import warnings

from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings("ignore")

# Carrega o banco de dados
arquivo = pd.read_csv('airline_passenger_satisfaction.csv', sep=',')

# Trata os valores - String para int
arquivo['Gender'] = arquivo['Gender'].replace('Female', 0)
arquivo['Gender'] = arquivo['Gender'].replace('Male', 1)

arquivo['customer_type'] = arquivo['customer_type'].replace('Loyal Customer', 0)
arquivo['customer_type'] = arquivo['customer_type'].replace('disloyal Customer', 1)

arquivo['type_of_travel'] = arquivo['type_of_travel'].replace('Personal Travel', 0)
arquivo['type_of_travel'] = arquivo['type_of_travel'].replace('Business travel', 1)

arquivo['customer_class'] = arquivo['customer_class'].replace('Eco Plus', 0)
arquivo['customer_class'] = arquivo['customer_class'].replace('Business', 1)
arquivo['customer_class'] = arquivo['customer_class'].replace('Eco', 2)

arquivo['satisfaction'] = arquivo['satisfaction'].replace('neutral or dissatisfied', 0)
arquivo['satisfaction'] = arquivo['satisfaction'].replace('satisfied', 1)

#Separa as variáveis preditoras da variável desfecho
y = arquivo['satisfaction']
x = arquivo.drop('satisfaction', axis = 1)

#Separa dados de treino de dados de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.4)


# MODELOS #

# Extra Trees Classifier #
tempo1begin = time.perf_counter()

modelo1 = ExtraTreesClassifier()
print("\n", modelo1.fit(x_treino,y_treino))

tempo1end = time.perf_counter()

# Logistic Regression #
tempo2begin = time.perf_counter()

modelo2 = LogisticRegression()
print("\n", modelo2.fit(x_treino, y_treino))

tempo2end = time.perf_counter()

# Random Forest Classifier #
tempo3begin = time.perf_counter()

modelo3 = RandomForestClassifier()
print("\n", modelo3.fit(x_treino, y_treino))

tempo3end = time.perf_counter()


# RESULTADOS #

resultado1 = modelo1.score(x_teste, y_teste)
resultado2 = modelo2.score(x_teste, y_teste)
resultado3 = modelo3.score(x_teste, y_teste)

tempo1 = tempo1end - tempo1begin
tempo2 = tempo2end - tempo2begin
tempo3 = tempo3end - tempo3begin

print("\nAcurácia Precisão Extra: %.3f Tempo: %.2fs"%(resultado1*100, tempo1))
print("\nAcurácia Regressão Logistica: %.3f Tempo: %.2fs"%(resultado2*100, tempo2))
print("\nAcurácia Floresta Aleatória: %.3f Tempo: %.2fs"%(resultado3*100, tempo3))