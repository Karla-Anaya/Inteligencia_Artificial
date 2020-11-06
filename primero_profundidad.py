import json
Grafo = False

with open ("arbol.json","r") as read_file:
	data = json.load(read_file)
	Grafo = data['Grafo']

def nodos(nodo,valor):
	lista = []
	aux=True
	for e in Grafo:
		if e["nodo"] == nodo:
			lista=e["ramas"].split()
	print (nodo,lista)
	if (lista[0] == valor):
		print ("Valor encontrado")
		return False
	else:
		while(len(lista)>=2):
			nodo = lista[1]
			lista.remove(nodo)
			aux=nodos(nodo,valor)
			if (aux==False):
				return False

nodos("Raiz","9")
