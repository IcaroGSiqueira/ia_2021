#Importação das bibliotecas
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#Definição dos valores de X e Y
X = [164, 166, 169, 171, 173, 176, 164, 166, 169, 171, 173, 176, 166, 169, 171, 171, 173, 178, 166, 169, 171, 173, 176, 178]
Y = [166, 171, 171, 171, 171, 173, 168, 173, 173, 173, 176, 176, 166, 166, 166, 176, 178, 176, 168, 168, 168, 168, 171, 178]
#Conversão de lista para vetor
data1 = np.array(X)
data2 = np.array(Y)
X = data1.reshape(-1,1)
Y = data2.reshape(-1,1)
#Criação do modelo
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,Y)
#Plotagem dos pontos X e Y
plt.scatter(X,Y)
plt.title('Regressão Linear Simples')
plt.xlabel('Altura média dos pais (cm)')
plt.ylabel('Altura dos filhos (cm)')
#Plotagem da reta que melhor se adapta aos pontos apresentados
plt.scatter(X,Y)
plt.plot(X, regressor.predict(X), color = 'red')
plt.title('Regressão Linear Simples')
plt.xlabel('Altura média dos pais (cm)')
plt.ylabel('Altura dos filhos (cm)')
#Resultados
score = regressor.score(X,Y)
print("Score: ", score)