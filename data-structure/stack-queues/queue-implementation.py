

class Node:
	def __init__(self, value):
		self.data = value
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first.data

	def enqueue(self, value):
		new_node = Node(value)
		if self.first == None:
			self.first = new_node
			self.last = self.first
			self.length += 1
		else:
			self.last.next = new_node
			self.last = new_node
			self.length += 1

	def dequeue(self):
		self.first = self.first.next
		self.length -= 1


	def printQ(self):
		temp = self.first
		print('\nQueue:', end = ' ')
		while temp != None:
			print(temp.data, end = ' <- ')
			temp = temp.next
		print(end = '[LAST]')
		print()


q = Queue()
q.enqueue('phil')
q.enqueue('bert')
q.enqueue('siapno')
#q.dequeue()
#q.dequeue()


print('peek:', q.peek())
q.printQ()






