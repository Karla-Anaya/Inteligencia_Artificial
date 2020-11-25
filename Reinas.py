def reinas(pl,pa):
	M = [[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]]
	cr = 0
	while (cr != 4 and pl < 4):
		while (M[pl][pa] != 0):
			if(pa != 3):
				pa += 1
			elif(pl != 3):
				pl += 1
				pa = 0
		M[pl][pa] = 1
		horizontal(pl,0,M)
		vertical(0,pa,M)
		diagonald(pl,pa,M)
		diagonali(pl,pa,M)
		pl +=1
		pa = 0
		cr += 1
	if (cr < 4):
		reinas(0,1)
	print ("numero de reinas",cr)
	for e in M:
		print (e)
	print ("")

def horizontal(l,a,M):
	while(a <= 3):
		if (M[l][a] == 0):
			M[l][a] = 2
		a += 1

def vertical(l,a,M):
	while(l <= 3):
		if (M[l][a] == 0):
			M[l][a] = 2
		l += 1

def diagonald(l,a,M):
	while(l <= 3 and a <= 3):
		if (M[l][a] == 0):
			M[l][a] = 2
		l += 1
		a += 1

def diagonali(l,a,M):
	while(l <= 3 and a >= 0):
		if (M[l][a] == 0):
			M[l][a] = 2
		l += 1
		a -= 1

reinas (0,0)
