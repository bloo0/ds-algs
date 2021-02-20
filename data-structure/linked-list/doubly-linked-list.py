


# append / prepend / insert / remove / printlist


class Node():
	def __init__(self, value):
		self.data = value
		self.next = None
		self.prev = None


class DoublyLinkeList():
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
			new_node.prev = self.tail 
			self.tail = new_node
			self.length += 1

	def prepend(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		self.length += 1

	def insert(self, index, value):
		new_node = Node(value)
		leader = self.traversetoindex(index - 1)
		placeholder = leader.next
		leader.next = new_node
		
		new_node.next = placeholder
		new_node.prev = leader

		placeholder.prev = new_node
		self.length += 1

	def remove(self,index):
		leader = self.traversetoindex(index - 1)
		placeholder = leader.next.next
		leader.next = placeholder
		placeholder.prev = leader
		self.length -= 1




	### SPECIAL FUNCTIONS
	def traversetoindex(self, index):
		curr_node = self.head
		i = 0
		while i != index:
			curr_node = curr_node.next
			i += 1
		return curr_node

	def printl(self):
		temp = self.head
		print(end = 'null  <<  ')
		while temp != None:
			print(temp.data, end = ' -> ')
			temp = temp.next
		print(end = ' null')
		print()



dl = DoublyLinkeList()
dl.append(10)
dl.append(5)
dl.append(16)
dl.append(17)
dl.append(18)

dl.prepend(2)

dl.insert(5,33)
dl.remove(5)

dl.printl()
print(dl.head.data, dl.tail.data)