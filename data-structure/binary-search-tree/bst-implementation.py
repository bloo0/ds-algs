
class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
			return
		else:
			curr_node = self.root
			while True:
				if value < curr_node.data:
					# LEFT
					if curr_node.left == None:
						curr_node.left = new_node
						return
					else:
						curr_node = curr_node.left
				elif value > curr_node.data:
					# RIGHT
					if curr_node.right == None:
						curr_node.right = new_node
						return
					else:
						curr_node = curr_node.right

	def lookup(self, value):
		curr_node = self.root
		while True:
			if curr_node == None:
				return False
			if curr_node.data == value:
				return True
			elif value < curr_node.data:
				curr_node = curr_node.left
			elif value > curr_node.data:
				curr_node = curr_node.right

	def remove(self, value):
		curr_node = self.root
		parent_node = None
		while True:
			if curr_node == None:
				return False
			if value < curr_node.data:
				parent_node = curr_node
				curr_node = curr_node.left
			elif value > curr_node.data:
				parent_node = curr_node
				curr_node = curr_node.right
			elif curr_node.data == value:
				# OPTION 1: No right child
				if curr_node.right == None:
					if parent_node == None:
						self.root = curr_node.left
					else:
						#if parent > current value, make current left child a child of parent
						if curr_node.data < parent_node.data:
							parent_node.left = curr_node.left
						#if parent < current value, make left child a right child of parent
						elif curr_node.data > parent_node.data:
							parent_node.right = curr_node.left

				# OPTION 2: Right child which doesnt have a left child
				elif curr_node.right.left == None:
					curr_node.right.left = curr_node.left
					if parent_node == None:
						self.root = curr_node.left
					else:
						# if parent > current, make right child of the left the parent
						if curr_node.data < parent_node.data:
							parent_node.left = curr_node.right
						# if parent < current, make right child a right child of the parent
						elif curr_node.data > parent_node.data:
							parent_node.right = curr_node.right

				# Right child that has a left child
				else:

					# find the right child left most child
					left_most = curr_node.right.left
					left_most_parent = curr_node.right
					while left_most.left != None:
						left_most_parent = left_most
						left_most = left_most.left

					# parent's left subtree is now left_most's right subtree
					left_most_parent.left = left_most.right
					left_most.left = curr_node.left
					left_most.right = curr_node.right

					if parent_node == None:
						self.root = left_most
					else:
						if curr_node.data < parent_node.data:
							parent_node.left = left_most
						elif curr_node.value > parent_node.data:
							parent_node.right = left_most
				return True



	def print_tree(self):
		if self.root != None:
			self.printt(self.root)

#Inorder Traversal (We get sorted order of elements in tree)
	

	def printt(self,curr_node):
		if curr_node != None:
			self.printt(curr_node.left)
			print(str(curr_node.data))
			self.printt(curr_node.right)


tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(6)
tree.insert(3)
tree.insert(12)
tree.insert(13)
tree.insert(11)

tree.remove(12)

x = tree.lookup(12)
print(x)


tree.print_tree()



