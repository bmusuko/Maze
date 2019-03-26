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
				jalurBFS = s	
				found = True
			else:
				if(y>0): 
					if(a[y-1][x] != 1):

						s.append((x-1,y))
						antrian.append((x,y-1,s))
						s.pop()
						print("Down")
				if(y<n-1): #top
					if(a[y+1][x] != 1):
						s.append((x+1,y))
						antrian.append((x,y+1,s))
						s.pop()
						print("Up")
				if(x<m-1): #right
					if(a[y][x+1] != 1):
						s.append((x,y+1))
						antrian.append((x+1,y,s))
						s.pop()
						print("Right")
				if(x>0): #left
					if(a[y][x-1] != 1):
						s.append((x,y-1))
						antrian.append((x-1,y,s))
						s.pop()
						print("left")
	found = False
	antrian = [(xawal,yawal,jarak(xawal,yawal,xakhir,yakhir),[xawal,yawal])]
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
				jalurBFS = s	
				found = True
			else:
				if(y>0): 
					if(a[y-1][x] != 1):
						s.append((x-1,y))
						antrian.append((x,y-1,f+jarak(x-1,y,xakhir,yakhir),s))
						s.pop()
						print("Down")
				if(y<n-1): #top
					if(a[y+1][x] != 1):
						s.append((x+1,y))
						antrian.append((x,y+1,f+jarak(x+1,y,xakhir,yakhir),s))
						s.pop()
						print("Up")
				if(x<m-1): #right
					if(a[y][x+1] != 1):
						s.append((x,y+1))
						antrian.append((x+1,y,f+jarak(x,y+1,xakhir,yakhir),s))
						s.pop()
						print("Right")
				if(x>0): #left
					if(a[y][x-1] != 1):
						s.append((x,y-1))
						antrian.append((x-1,y,f+jarak(x,y-1,xakhir,yakhir),s))
						s.pop()
						print("left")
		antrian = sorted(antrian,key=lambda x:x[2])
		#print(antrian)


if __name__ == '__main__':
	main()

