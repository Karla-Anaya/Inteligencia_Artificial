import json
with open ("json_caballos.json","r") as read_file:
	data = json.load(read_file)
	Grafo = data['Grafo']
	E_ini = data['E_ini']
	E_final = data['E_final']

def caballos(Mat,fin,op):
	M=[[0,0,0],
[0,0,0],
[0,0,0]]
	l = 0
	while(l < 3):
		a = 0
		while(a < 3):
			if (Mat[l][a] != 0):
				digito = Mat[l][a]
				Mat[l][a] = 0
				busqueda(l,a,digito,M,op)
			a +=1
		l +=1
	for e in M:
		print (e)
	print ("")
	if (M != E_final):
		return caballos(M,fin,op)

def busqueda(pos_l,pos_a,digito,M,op):
	elemento = Ma[pos_l][pos_a]
	for e in Grafo:
		if (elemento == e[0]):
			l = 0
			while(l <= 2):
				a = 0
				while(a <= 2):
					if (Ma[l][a] == e[op]):
						M[l][a] = digito
						return M
					a += 1
				l += 1

Ma=[[0,1,2],
[3,4,5],
[6,7,8]]
op = int(input("Recorrido por derecha (1),Recorrido por izquierda (2): "))
if (op < 1 or op > 2):
	print ("Error debes ingresar una de las dos opciones dadas (1 o 2)")
	quit()
caballos(E_ini,E_final,op)
