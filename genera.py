import json
Conocimiento = False
palabras = ["a","e","o","con", "la","de","el","los","al","es","de"]

with open ("tweets.json","r") as read_file:
	data = json.load(read_file)
	Conocimiento = data['tweets']

def stream(con):
	lista = []
	for e in con:
		if e["Stream"] == True:
			lista.append(e["texto"].split())
	return elimina(lista)

def elimina(lista):
	aux = []
	lf = []
	r = []
	for e in lista:
		c = 0
		while (c < len(e)):
			if (e[c] not in palabras):
				aux = aux + [e[c]]
			c += 1
	for i in aux:
		if i not in r:
			r.append(i)
			porcentaje = (aux.count(i)/(len(lista)))
			lf.append([i,porcentaje])
	return crea(lf)

def crea(lista):
    dic = {}
    dic["Probabilidades"] = lista
    with open ("Matriz.json","w") as file:
        json.dump(dic,file)
        return ("Matriz creada :",dic)
 
print(stream(Conocimiento))
