import numpy as np
#Primeira reta
m = 7
b = 1
L = 0.000001 #Learning rate
iteracoes = 5
amostras = 24
#Definindo valores de X e Y
X = [164, 166, 169, 171, 173, 176, 164, 166, 169, 171, 173, 176, 166, 169, 171, 171, 173, 178, 166, 169, 171, 173, 176, 178]
Y = [166, 171, 171, 171, 171, 173, 168, 173, 173, 173, 176, 176, 166, 166, 166, 176, 178, 176, 168, 168, 168, 168, 171, 178]
#Criando o gradiente descendente
for i in range(iteracoes):
  for j in range(amostras):   
    Y_pred = m*X[j] + b #valor atual da reta
    derivadam = np.sum(2*X[j]*(Y_pred - Y[j])) #derivada da função de custo em relação a m
    derivadab = np.sum(2*(Y_pred - Y[j])) #derivada da função de custo em relação a b
    m = m + derivadam * L #atualiza m
    b = b + derivadab * L #atualiza m
  print('valor m: ', m, 'valor b: ', b)