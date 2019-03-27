from copy import deepcopy
import math

def jarak(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def main():
	file = open("input.txt","r")
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
	#b = a.copy()
	for j in range (n):
		if(a[j][0] == 0):
			xawal = 0
			yawal = j
			break
	for j in range (n):
		if(a[j][m-1] == 0):
			xakhir = m-1
			yakhir = j
			break
	#xawal = 2
	#yawal = 0
	#xakhir = 2
	#yakhir = 4
	telusurBFS = 0
	print(xawal,yawal,xakhir,yakhir,n,m)
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
	if(found):
		print(jalurBFS)
		print("penelusuran BFS sebanyak : ",telusurBFS)
	found = False
	antrian = [(xawal,yawal,jarak(xawal,yawal,xakhir,yakhir),[(xawal,yawal)])]
	
	telusurAstar = 0
	a = deepcopy(b)
	while not found: # A*
		#print(antrian)
		if(len(antrian) == 0):
			print("maze buntu")
			break
		else:
			x,y,f,s = antrian.pop(0)
			a[y][x] = 1
			#print(x,y)
			if(x == xakhir and y == yakhir):
				jalurAStar = deepcopy(s)
				found = True
			else:
				if(y>0): #down 
					if(a[y-1][x] != 1):
						telusurAstar += 1
						l = deepcopy(s)
						l.append((x,y-1))
						antrian.append((x,y-1,f+jarak(x-1,y,xakhir,yakhir),l))
						#print("Down")
				if(y<n-1): #top
					if(a[y+1][x] != 1):
						telusurAstar += 1
						t = deepcopy(s)
						t.append((x,y+1))
						antrian.append((x,y+1,f+jarak(x+1,y,xakhir,yakhir),t))
						#print("Up")
				if(x<m-1): #right
					if(a[y][x+1] != 1):
						telusurAstar += 1
						r = deepcopy(s)
						r.append((x+1,y))
						antrian.append((x+1,y,f+jarak(x,y+1,xakhir,yakhir),r))
						#print("Right")
				if(x>0): #left
					if(a[y][x-1] != 1):
						telusurAstar += 1
						le = deepcopy(s)
						le.append((x-1,y))
						antrian.append((x-1,y,f+jarak(x,y-1,xakhir,yakhir),le))
						#print("left")

		antrian = sorted(antrian,key=lambda x:x[2])
		
	if(found):
			print(jalurAStar)
			print("penelusuran A* sebanyak : ",telusurAstar)


if __name__ == '__main__':
	main()

