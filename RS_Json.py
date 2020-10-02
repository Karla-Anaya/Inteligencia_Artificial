import json
C = False
with open("Base.json","r") as read_file:
	data = json.load(read_file)
	C= data['conocimiento']

def funciones(A,V,B,Conocimiento):
	i=0
	while i<len(Conocimiento):
		aux=Conocimiento[i]
		if aux[1]==V:
			if ((aux[0]==A) and (aux[2]==B)):
				return True
		i+=1
	return False

def animales(A,V,B):
	if ((V == "Es") or (V == "Tiene") or (V == "Vive")):
		return funciones(A,V,B,C)
	else:
		print ("Use un verbo correcto")
		return 

def main():
	Fin=False
	print ('Este programa funciona poniendo la siguiente sintaxis: animales("<Animal>","<Verbo>","<Caranteristica>")')
	print('Verbos permitidos "Es","Tiene","Vive". ')
	print ("Recuerda usar la primera letra en mayuscula")
	while not Fin:
		Entrada = input("-->")
		if (Entrada == 'q'):
			quit()
		if not Entrada:
			print ("No se ingreso nada")
		else:
			print (eval(Entrada))

if __name__ == "__main__":
	main()
