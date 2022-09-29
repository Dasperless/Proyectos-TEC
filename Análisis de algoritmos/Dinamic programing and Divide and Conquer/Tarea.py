import sys

#Funcion para obtener el indice del primer elemento  mayor o igual a A[i]
def searchId(arr, n, x):

	# Indice inicial y final
	low = 0  
	high = n

	# Mientras el indice inicial sea menor el final
	while low < high:

		mid = low + int((high - low) / 2)

		if x <= arr[mid]:
			high = mid

		else:
			low = mid + 1

	return low

# Funcion que devuelve el string el 
def longIncSubDC(a, n):

	temp = [sys.maxsize]*n
	position = [] 	#array de posiciones

	pt = 0 	#Posicion del ultimo elemento en el arreglo temporal

	temp[0] = ord(a[0]) #Posiciona el primer elemento en temp
	position.append(0)	#Indice del primer elemento

	for i in range(1, n):
		#Agregar si a[i] es mayor que el ultimo elemento de la lista temporal
		if temp[pt] < ord(a[i]):
			temp[pt + 1] = ord(a[i])
			position.append(i)
			pt = pt + 1
		else:
			#si a[i] es mayor, lo coloca en la posición adecuada tal que temp[ind-1]<a[i]
			ind = searchId(temp, n, ord(a[i]))
			temp[ind] = ord(a[i])
			position[ind] = i

	res = ""
	for i in range(pt + 1):
		res += a[position[i]]	
	return res
	
def longIncSubDP(a, n):
	lis = [1]*n
	parent = [-1]*n

	for i in range(n):
		for j in range(i):
			if a[j] < a[i]:
				if lis[i] < lis[j] + 1:
					lis[i] = lis[j] + 1
					parent[i] = j

	length = 0
	pos = 0
	for i in range(n):
		if length < lis[i]:
			length = lis[i]
			pos = i

	sequence = []

	while pos != -1:
		sequence.append(a[pos])
		pos = parent[pos]

	sequence.reverse()

	res = ""
	for i in range(length):
		res+=sequence[i]
	return res
		
a = "XFDASCXQWGFBH"

n = len(a)

print(longIncSubDC(a, n))
print(longIncSubDP(a, n))

#Se hacen varias veces el calculo de la posicion del último número