
class Graph:
	def __init__(self):
		self.numberOfNodes = 0
		self.adjacentList = {}

	def __str__(self):
		return str(self.__dict__)

	def addVertex(self, node):
		self.adjacentList[node] = []
		self.numberOfNodes += 1

	def addEdge(self, node1, node2):
		self.adjacentList[node1].append(node2)
		self.adjacentList[node2].append(node1)


	## checker
	def showConn(self):
		for i in self.adjacentList:
			print(i, end = ' --> ')
			for j in self.adjacentList[i]:
				print(j, end = ' ')
			print()



g = Graph()

g.addVertex('0')
g.addVertex('1')
g.addVertex('2')
g.addVertex('3')
g.addVertex('4')
g.addVertex('5')
g.addVertex('6')

g.addEdge('0','1')
g.addEdge('0','2')
g.addEdge('1','2')
g.addEdge('1','3')
g.addEdge('2','4')
g.addEdge('3','4')
g.addEdge('4','5')
g.addEdge('5','6')


g.showConn()
print(g)













