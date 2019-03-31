from copy import deepcopy
import math

def jarak(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def solveBFS(filename):
	file = open(filename,"r")
	a = []
	n = 0
	for line in file:
		y = line.rstrip()
		temp = []
		for c in y:	
			temp.append(int(c))
		a.append(temp)
		n += 1
	m = len(a[0])
	a.reverse()
	b = deepcopy(a)
	maze = deepcopy(a)
	#b = a.copy()
	found = False
	c = 0 
	
	for j in range (n):
		if(a[j][0] == 0):
			if(c==0):
				xawal = 0
				yawal = j
				c += 1
			elif(c==1):
				xakhir = 0
				yakhir = j
				c += 1
	
	for j in range(m):
		if(a[n-1][j] == 0):
			if(c==0):
				xawal = j
				yawal = m-1
				c += 1
			elif(c==1):
				xakhir = j
				yakhir = m-1
				c += 1
	
	for j in range (n):
		if(a[j][m-1] == 0):
			if(c==0):
				xawal = m-1
				yawal = j
				c += 1
			elif(c==1):
				xakhir = m-1
				yakhir = j
				c += 1 
	for j in range(m):
		if(a[0][j] == 0):
			if(c== 0):	
				xawal = j
				yawal = 0
			elif(c==1):
				xakhir = j
				yakhir = 0
				c += 1

	telusurBFS = 0
	#print(xawal,yawal,xakhir,yakhir,n,m)
	antrian = [(xawal,yawal,[(xawal,yawal)])]		
	found = False
	while not found: # BFS
		#print(antrian)
		if(len(antrian) == 0):
			print("maze buntu")
			break
		else:
			x,y,s = antrian.pop(0)
			a[y][x] = 1
			#print(x,y)
			if(x == xakhir and y == yakhir):
				jalurBFS = deepcopy(s)	
				found = True
			else:
				if(y>0): 
					if(a[y-1][x] != 1):
						telusurBFS += 1
						l = deepcopy(s)
						l.append((x,y-1))
						antrian.append((x,y-1,l))
						#print("Down")
				if(y<n-1): #top
					if(a[y+1][x] != 1):
						telusurBFS += 1
						t = deepcopy(s)
						t.append((x,y+1))
						antrian.append((x,y+1,t))
						#print("Up")
				if(x<m-1): #right
					if(a[y][x+1] != 1):
						telusurBFS += 1
						r = deepcopy(s)
						r.append((x+1,y))
						antrian.append((x+1,y,r))
						#print("Right")
				if(x>0): #left
					if(a[y][x-1] != 1):
						telusurBFS += 1
						le = deepcopy(s)
						le.append((x-1,y))
						antrian.append((x-1,y,le))
						#print("left")
	"""
	if(found):
		print(jalurBFS)
		print("penelusuran BFS sebanyak : ",telusurBFS)
	"""
	for (x,y) in jalurBFS:
		maze[y][x] = 2
		
	maze.reverse()
	ans = open("ans.txt", "w+")
	i = len(maze)
	for lines in maze:
		for x in lines:
			ans.write(str(x))
		if (i > 1):
			ans.write('\n')
			i = i - 1

def solveAStar(filename):
	file = open(filename,"r")
	a = []
	n = 0
	for line in file:
		y = line.rstrip()
		temp = []
		for c in y:	
			temp.append(int(c))
		a.append(temp)
		n += 1
	m = len(a[0])
	a.reverse()
	b = deepcopy(a)
	maze = deepcopy(a)
	#b = a.copy()
	found = False
	c = 0 
	
	for j in range (n):
		if(a[j][0] == 0):
			if(c==0):
				xawal = 0
				yawal = j
				c += 1
			elif(c==1):
				xakhir = 0
				yakhir = j
				c += 1
	
	for j in range(m):
		if(a[n-1][j] == 0):
			if(c==0):
				xawal = j
				yawal = m-1
				c += 1
			elif(c==1):
				xakhir = j
				yakhir = m-1
				c += 1
	
	for j in range (n):
		if(a[j][m-1] == 0):
			if(c==0):
				xawal = m-1
				yawal = j
				c += 1
			elif(c==1):
				xakhir = m-1
				yakhir = j
				c += 1 
	for j in range(m):
		if(a[0][j] == 0):
			if(c== 0):	
				xawal = j
				yawal = 0
			elif(c==1):
				xakhir = j
				yakhir = 0
				c += 1

	found = False
	antrian = [(xawal,yawal,jarak(xawal,yawal,xakhir,yakhir),0,[(xawal,yawal)])] #[(x,y,f,g,[(x,y)])]
	
	telusurAstar = 0
	a = deepcopy(b)
	#print(antrian)
	while not found: # A*
		#print(antrian)
		if(len(antrian) == 0):
			print("maze buntu")
			break
		else:
			x,y,f,g,s = antrian.pop(0)
			a[y][x] = 1
			g += 1
			#print(x,y)
			if(x == xakhir and y == yakhir):
				jalurAStar = deepcopy(s)
				
				found = True
				#print(f)
			else:
				if(y>0): #down 
					if(a[y-1][x] != 1):
						telusurAstar += 1
						l = deepcopy(s)
						l.append((x,y-1))
						antrian.append((x,y-1,g+jarak(x,y-1,xakhir,yakhir),g,l))
						#print("Down")
				if(y<n-1): #top
					if(a[y+1][x] != 1):
						telusurAstar += 1
						t = deepcopy(s)
						t.append((x,y+1))
						antrian.append((x,y+1,g+jarak(x,y+1,xakhir,yakhir),g,t))
						#print("Up")
				if(x<m-1): #right
					if(a[y][x+1] != 1):
						telusurAstar += 1
						r = deepcopy(s)
						r.append((x+1,y))
						antrian.append((x+1,y,g+jarak(x+1,y,xakhir,yakhir),g,r))
						#print("Right")
						#print(x,y+1,xakhir,yakhir)
				if(x>0): #left
					if(a[y][x-1] != 1):
						telusurAstar += 1
						le = deepcopy(s)
						le.append((x-1,y))
						antrian.append((x-1,y,g+jarak(x-1,y,xakhir,yakhir),g,le))
						#print("left")

		antrian = sorted(antrian,key=lambda x:x[2])
		#print(antrian)
		
	"""
		if(found):
			print(jalurAStar)
			#print(antrian)
			print ("penelusuran A* sebanyak : ",telusurAstar)

	"""
	for (x,y) in jalurAStar:
		maze[y][x] = 2
	"""
	for m in maze :
		print(m)		
	"""
	maze.reverse()
	ans = open("ans.txt", "w+")
	i = len(maze)
	for lines in maze:
		for x in lines:
			ans.write(str(x))
		if (i > 1):
			ans.write('\n')
			i = i - 1