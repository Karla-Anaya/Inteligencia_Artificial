import json
cono = False
f = open ("tweet.txt","r")
tweet = f.read()
tweet = tweet.split()
print (tweet)
with open ("Json.json", "r") as read_file:
	data = json.load(read_file)
	cono = data['probabilidades']

def compara(T,CON):
	x = 0 
	y = 0
	aux = []
	for x in range(len(T)):
		for y in range(len(CON)):
			pila = T[x]
			Elemento = CON[y]
			if Elemento[0] == pila:
				aux.append(CON[y])
			if x == len (T) -1 and y == len (CON) -1:
				return promedio(aux)
    
def promedio(Aux):
	i = 0
	suma = 0
	valido = 0.55
	while (i < len(Aux)):
		Element = Aux[i][1]
		suma = suma + float(Element)
		i += 1    
	resultado = suma / len(Aux)
	print ("La posibilidad de que sea Stream es del :",resultado,"%")
	if resultado >= valido:
		print("Hay Stream")
	else:
		print("No hay stream")

compara(tweet,cono)
