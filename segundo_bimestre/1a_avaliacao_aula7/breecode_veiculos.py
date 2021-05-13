from sklearn import tree

ciclomotor = 0
helicoptero = 1
carro = 2
lancha = 3

# Peso, N. Helice, N. Porta, N. Roda
breed = [
[200,	0,	0,	2],
[600,	2,	2,	0],
[1200,	0,	2,	4],
[500,	1,	0,	0],
[300,	0,	0,	3],
[1900,	3,	4,	3],
[900,	2,	0,	0],
[1200,	2,	3,	3],
[2000,	0,	4,	4],
[800,	1,	1,	0]
]

result = [
ciclomotor,
helicoptero,
carro,
lancha,
ciclomotor,
helicoptero,
lancha,
helicoptero,
carro,
lancha
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(breed, result)

peso = input("Digite o Peso: ")
helice = input("Digite o nro. de Helices: ")
porta = input("Digite o nro. de Portas: ")
roda = input("Digite o nro. de Rodas: ")

resultadoUsuario = clf.predict([[peso, helice, porta, roda]])

if resultadoUsuario == 0:
	print("É um Ciclomotor!")
elif resultadoUsuario == 1:
	print("É um Helicoptero!")
elif resultadoUsuario == 2:
	print("É um Carro!")
else:
	print("É um Lancha!")