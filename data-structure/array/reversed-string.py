

def reversedStr(a):
	container = []
	for i in range(len(a) - 1, -1, -1):
		container.append(a[i])
	return ''.join(container)


print(reversedStr('My name is phil'))