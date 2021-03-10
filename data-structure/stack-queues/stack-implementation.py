



# array implementation
class ArrayStacks:
	def __init__(self):
		self.list = []
		self.length = 0

	def __str__(self):
		return str(self.__dict__)

	def push(self, value):
		self.list.append(value)
		self.length += 1

	def peek(self):
		return self.list[self.length - 1]

	def pop(self):
		del self.list[self.length - 1]
		self.length -= 1





# linked-list implementation
class Node:
	def __init__(self, value):
		self.data = value
		self.next = None
		

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def push(self, value):
		new_node = Node(value)
		if self.bottom == None:
			self.bottom = new_node
			self.top = self.bottom
			self.length += 1
		else:
			new_node.next = self.top
			self.top = new_node
			self.length += 1

	def peek(self):
		return self.top.data

	def pop(self):
		self.top = self.top.next


	def printStack(self):
		temp = self.top
		print('\n- stack -')
		while temp != None:
			print(temp.data)
			temp = temp.next
		print()


s = Stack()
s.push('google')
s.push('youtube')
s.push('udemy')
s.push('discord')
#s.pop()
#s.pop()

print('top:', s.peek())

s.printStack()









