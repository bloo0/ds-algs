


arr = [64, 34, 25, 12, 22, 11, 90] 


# bubble sort alg
def sort0(a):
	for i in range(len(a)): # traverse / movement
		for j in range(len(a) - i - 1): # j is used to access values
			if a[j] < a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a


# insert sort alg
def sort1(a):
	for i in range(1, len(a)): # traverse / movement
		key = a[i]
		j = i - 1 # for while loop
		while j >= 0 and key < a[j]: # j is used to access values
			a[j+1] = a[j]
			j -= 1 # will break while loop
		print(a)
		a[j+1] = key # values do not move, they are copied. key is being set to proper position
		print(a)
	return a


# selection sort
def sort2(a):
	pass

print(f'\n{sort1(arr)}')
