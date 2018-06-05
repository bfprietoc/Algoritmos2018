def tiling(n):
	A = [0 for i in range(n+1)] 
	C = [0 for i in range(n+1)] 
	D = [0 for i in range(n+1)]
	D[0] = A[1] = 1
	for i in range(2, n+1): 
		C[i] = A[i-1]
		A[i] = D[i-1] + C[i-1]
		D[i] = D[i-1] + 2*A[i-1]

	return D[n]

print(tiling(10)) 
print(tiling(50)) 
print(tiling(100))
