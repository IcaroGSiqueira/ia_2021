#
#                                       0
#                                                                              
#                   1                                      2
#                                                                              
#         3                   4                  5                   6
#                                                                              
#    7         8         9        10        11        12        13        14
#                                                                              
# 15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30

import time

origem = 0
destino = 6

#grafos em python dictionary
arvore1 =  {
	0 : [(1,3),(2,1)],
	1 : [(3,4),(4,4)],
	2 : [(5,2),(6,0)],
	3 : [(7,5), (8,5)],
	4 : [(9,5), (10,5)],
	5 : [(11,3), (12,3)],
	6 : [(13,1), (14,1)],
	7 : [(15,6), (16,6)],
	8 : [(17,6), (18,6)],
	9 : [(19,6), (20,6)],
	10 : [(21,6), (22,6)],
	11 : [(23,4), (24,4)],
	12 : [(25,4), (26,4)],
	13 : [(27,2), (28,2)],
	14 : [(29,2), (30,2)],
	15 : [],
	16 : [],
	17 : [],
	18 : [],
	19 : [],
	20 : [],
	21 : [],
	22 : [],
	23 : [],
	24 : [],
	25 : [],
	26 : [],
	27 : [],
	28 : [],
	29 : [],
	30 : []
}

arvore2 =  {
	0 : [(1,3),(2,1)],
	1 : [(3,4),(4,4)],
	2 : [(5,2),(6,0)],
	3 : [(7,5), (8,5)],
	4 : [(9,5), (10,5)],
	5 : [(11,3), (12,3)],
	6 : [(13,1), (14,1)],
	7 : [],
	8 : [],
	9 : [],
	10 : [],
	11 : [],
	12 : [],
	13 : [],
	14 : []
}

arvore3 =  {
	0 : [(1,3),(2,1)],
	1 : [(3,4),(4,4)],
	2 : [(5,2),(6,0)],
	3 : [],
	4 : [],
	5 : [],
	6 : []
}

def buscaGulosa(graph, node, search):
	nodoAtual = node
	caminho = []
	caminho.append(nodoAtual)
	distancia = 0
	while len(set([nodoVizinho for (nodoVizinho, distance) in graph.get(nodoAtual, [])]).difference(set(caminho))) > 0:
		vizinhoProximo = None
		menorDistancia = None
		for vizinho, vizinhoDistancia in graph[nodoAtual]:
			if vizinho != nodoAtual and vizinho not in caminho:
				if menorDistancia is not None:
					if menorDistancia > vizinhoDistancia:
						menorDistancia = vizinhoDistancia
						vizinhoProximo = vizinho
				else:
					menorDistancia = vizinhoDistancia
					vizinhoProximo = vizinho
		vizinhoMaisProximo = (vizinhoProximo, menorDistancia)
		nodoAtual = vizinhoMaisProximo[0]
		caminho.append(nodoAtual)
		distancia += vizinhoMaisProximo[1]
		if nodoAtual == search:
			fim = time.time()
			print("caminho: %s" %caminho)
			print("distancia: %d" %distancia)
			print("Tempo: %fs" %(fim - inicio))
			return 0

inicio = time.time()

buscaGulosa(arvore1, origem, destino)


