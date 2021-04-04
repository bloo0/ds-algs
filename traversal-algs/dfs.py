
#
# 	    101
#	33		105
# 
# inorder - [33, 101, 105]
# preorder - [101, 33, 105]
# postorder - [33, 105, 101]
#


#
#		9
#   4		 20
# 1	  6	  15    170
#
# inorder - [1, 4, 6, 9, 15, 20, 170]
# preorder - [9, 4, 1, 6, 20, 15, 170]
# postorder - [1, 6, 4, 15, 170, 20, 9]
#

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,val):
    new_node = Node(val)
    if self.root == None:
      self.root = new_node
      return 
    temp = self.root
    while True:
      if new_node.val < temp.val:
        if temp.left == None:
          temp.left = new_node
          break
        else:
          temp = temp.left
      elif new_node.val > temp.val:
        if temp.right == None:
          temp.right = new_node
          break
        else:
          temp = temp.right

  def lookup(self,val):
    temp = self.root
    while True:
      if temp.val == val:
        return True
      elif temp == None:
        return False
      elif val < temp.val:
        temp = temp.left
      elif val > temp.val:
        temp = temp.right

  def inorder(self,currnode,mylist):
    pass

  def preorder(self,currnode,mylist):
    pass

#According to Andre's video , below is easily understandable

  def postorder(self,currnode,mylist):
    pass
    
      
    

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inorder(tree.root,[]))
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))

