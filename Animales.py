Conocimiento_es = [
	("Tortuga", "Oviparo"),
	("Gallo", "Oviparo"),
	("Cocodrilo", "Oviparo"),
	("Iguana", "Oviparo"),
	("Gato", "Viviparo"),
	("Ballena","Viviparo"),
	("Oso", "Viviparo"),
	("Delfin", "Viviparo"),
	("Viviparo","Mammalia"),
	("Mammalia","G. Mamarias"),
	("Mammalia","Tetrapodo"),
	("Oviparo", "Sauropsidos"),
	("Sauropsidos","Tetrapodo"),
	("Tetrapodo","Vertebrado")
]

Conocimiento_tiene = [
	("Gato", "Pelo","Garras"),
	("Oso", "Pelo", "Garras"),
	("Delfin", "P. Queratina",""),
	("Ballena", "P. Queratina",""),
	("Tortuga", "P. Queratina","Garras"),
	("Iguana", "P. Queratina","Garras"),
	("Gallo", "P. Queratina","Garras"),
	("Cocodrilo", "P. Queratina","Garras")
]

Conocimiento_vive = [
	("Cocodrilo", "Tierra"),
	("Delfin", "Agua"),
	("Ballena", "Agua"),
	("Gato", "Tierra"),
	("Oso", "Tierra"),
	("Tortuga", "Tierra"),
	("Iguana", "Tierra"),
	("Gallo", "Tierra"),
]

##gato, vert

def animales(A,B):
	aux1=es(A,B,Conocimiento_es)
	if aux1 == False:
		print (A,B)
		aux2=tiene(A,B,Conocimiento_tiene)
		if aux2 == False:
			aux3=vive(A,B,Conocimiento_vive)
			if aux3 == False:
				return False
			else:
				return True
		else:
			return True
	else:
		return True
		
	
def es(A,B,Conocimiento_es):
	i=0
	while i<len(Conocimiento_es):
		aux=Conocimiento_es[i]
		if aux[0]==A:
			if aux[1]==B:
				return True
			else:
				return es(aux[1],B,Conocimiento_es)
		i+=1
	return False
	


def tiene(A,B,Conocimiento_tiene):
	i=0
	while i<len(Conocimiento_tiene):
		aux=Conocimiento_tiene[i]
		if aux[0]==A:
			if aux[1]==B or aux[2]==B:
				return True
			else:
				return tiene(aux[1],B,Conocimiento_tiene)
		i+=1
	return False
	

def vive(A,B,Conocimiento_vive):
	i=0
	while i<len(Conocimiento_vive):
		aux=Conocimiento_vive[i]
		if aux[0]==A:
			if aux[1]==B:
				return True
			else:
				return vive(aux[1],B,Conocimiento_vive)
		i+=1
	return False


print(animales("Cocodrilo","Tierra"))
