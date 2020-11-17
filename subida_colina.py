import json
import random
Grafo = False

with open ("json_sc.json","r") as read_file:
	data = json.load(read_file)
	Grafo = data['Grafo']

def subida(nodoi,nodof):
	op = []
	lv = []
	ln = []
	for e in Grafo:
		if (e["nodo"]==nodoi):
			op = e["Opciones"]
	m = op[0][0]
	for i in op:
		if m > i[0]:
			lv = i[0]
			ln = i[1]
			m = i[0]
		elif (m == i[0]):
			lv += i[0]
			ln += i[1]
	for k in op:
		if (len(ln)>1):
			L = random.choice(ln)
			if(L == nodof):
				print (m,L)
				return True
			else:
				print (m,L)
				return subida(L, nodof)
		if k[0] == m:
			if k[1] == nodof:
				print (m,k[1])
				return True
			else:
				print (m,k[1])
				return subida(k[1],nodof)

R = subida("A","E")
if (R):
	print ("Se llego al nodo ")
