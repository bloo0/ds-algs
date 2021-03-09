


# append / prepend / insert / remove / printlist


class Node():
	def __init__(self, value):
		self.data = value
		self.next = None


class LinkeList():
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, value):
		new_node = Node(value)
		if self.head == None:
			self.head = new_node
			self.tail = self.head
			self.length = 1
		else:
			self.tail.next = new_node
			self.tail = new_node
			self.length += 1

	def prepend(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		self.length += 1

	def insert(self, index, value):
		if index >= self.length:
			self.append(value)

		new_node = Node(value)
		temp = self.head
		i = 0
		while i < self.length:
			if i == index - 1:
				temp.next, new_node.next = new_node, temp.next
				self.length += 1
				break

			temp = temp.next
			i += 1

	def remove(self,index):
		temp = self.head
		i = 0
		while i < self.length:
			if i == index - 1:
				temp.next = temp.next.next
				self.length -= 1
				break

			temp = temp.next
			i += 1


	### SPECIAL FUNCTIONS
	def reverse(self):
		prev = None
		self.tail = self.head
		while self.head != None:
			temp = self.head
			self.head = temp.next
			temp.next = prev
			prev = temp
		self.head = temp

	def printl(self):
		temp = self.head
		while temp != None:
			print(temp.data, end = ' -> ')
			temp = temp.next
		print(end = 'null')
		print()



l = LinkeList()
l.append(10)
l.append(5)
l.append(16)
l.append(17)
l.append(18)

l.prepend(2)

l.insert(4,33)
l.remove(5)

l.reverse()

l.printl()
print(l.head.data, l.tail.data)