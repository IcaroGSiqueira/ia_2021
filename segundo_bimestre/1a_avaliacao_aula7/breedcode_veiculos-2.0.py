from sklearn import tree

ciclomotor = 0 # moto / quadriciclo / triciclo
helicoptero = 1
carro = 2
lancha = 3

# Peso, N. Helice, N. Porta, N. Roda, Lugares
breed = [
[1700,	2,	4,	0, 5], # helicoptero
[650,	0,	0,	0, 7], # lancha
[200,	0,	0,	2, 2], # ciclomotor
[600,	2,	2,	0, 2], # helicoptero
[1200,	0,	2,	4, 5], # carro
[500,	1,	0,	0, 2], # lancha
[550,	0,	0,	3, 2], # ciclomotor
[1900,	3,	4,	3, 10], # helicoptero
[700,	0,	1,	3, 2], # carro
[150,	0,	0,	2, 1], # ciclomotor
[900,	2,	0,	0, 6], # lancha
[1200,	2,	3,	3, 14], # helicoptero
[2000,	0,	4,	4, 8], # carro
[800,	1,	1,	0, 5], # lancha
[350,	0,	0,	4, 2], # ciclomotor
[750,	0,	0,	4, 2] # carro
]

result = [
helicoptero,
lancha,
ciclomotor,
helicoptero,
carro,
lancha,
ciclomotor,
helicoptero,
carro,
ciclomotor,
lancha,
helicoptero,
carro,
lancha,
ciclomotor,
carro
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(breed, result)

peso = input("Digite o Peso: ")
helice = input("Digite o nro. de Helices: ")
porta = input("Digite o nro. de Portas: ")
roda = input("Digite o nro. de Rodas: ")
lugares = input("Digite o nro. de Lugares: ")

resultadoUsuario = clf.predict([[peso, helice, porta, roda, lugares]])

if resultadoUsuario == 0:
	print("É um Ciclomotor!")
elif resultadoUsuario == 1:
	print("É um Helicoptero!")
elif resultadoUsuario == 2:
	print("É um Carro!")
else:
	print("É um Lancha!")