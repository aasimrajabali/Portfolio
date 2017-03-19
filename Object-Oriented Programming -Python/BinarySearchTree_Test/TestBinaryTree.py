#  File: TestBinaryTree.py

#  Description: This program tests helper functions for a binary search tree

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: April 18,2015

#  Date Last Modified: April 19, 2015

class Node (object):
    
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

  def insert(self,data):
      
      if self.data == data:
          return False
        
      elif data < self.data:
          if self.lChild:
              return self.lChild.insert(data)
          else:
              self.lChild = Node(data)
              return True
            
      else:
          if self.rChild:
              return self.rChild.insert(data)
          else:
              self.rChild = Node(data)
              return True
            
  def inOrder(self, a):
      
      if self:
          if self.lChild:
              self.lChild.inOrder(a)
          a.append(self.data)
          if self.rChild:
              self.rChild.inOrder(a)
      return a
    
  #returns true if two trees are equal 
  def isSimilar(self,other):
      
      if other == None:
          return False
      if self.data != other.data:
          return False
      eq = True

      if self.lChild == None:
          if other.lChild:
              return False
      else:
          eq = self.lChild.isSimilar(other.lChild)
      if eq == False:
          return False
        
      if self.lChild == None:
          if other.rChild:
              return False
      else:
          eq = self.rChild.isSimilar(other.rChild)
          
      return eq
    
  #prints the nodes for a given level, assuming the level is valid
  def printLevel(self,level,):
      
      if self == None:
          return None
      if level == 1:
          print(self.data, end=' ')
      else:
          self.lChild.printLevel(level - 1)
          self.rChild.printLevel(level - 1)
          
  #returns the height of a tree (the longest path to a leaf) 
  def getHeight(self,height=0):
      
      if self.lChild == None:
          return height
      else:
          return self.lChild.getHeight(height + 1)

      if self.rChild == None:
          return height
      else:
          return self.rChild.getHeight(height + 1)

  def getNodes_right(self):
      
      current = self
      if current == None:
          return 0
      else:
          if (current.lChild == None):
              return 0
          else:
              return(1 + current.lChild.getNodes_right()) \
                       + (current.rChild.getNodes_right())
      
  def getNodes_left(self):
      
      current = self
      if current == None:
          return 0
      else:
          if (current.rChild == None):
              return 0
          else:
              return(1 + current.lChild.getNodes_left()) \
                       + (current.rChild.getNodes_left())
          

class Tree (object):
    
  def __init__ (self):
    self.root = None
    
  def insert(self,data):
      #if the root node exists, there's at least one node in the tree
      if self.root:
          return self.root.insert(data)
      else:
          self.root = Node(data)
          return True
        
  #search for a node given the key  
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  def inOrder(self,a):
    self.root.inOrder(a)
    
  
  def isSimilar(self, other):
      if(self.root.isSimilar(other.root)):
          return True
      return False
      
  #function to traverse through each tree in inOrder and append the values
  def insert_val(self, a):
    for i in a:
        self.insert(i)
  
  def printLevel(self,level):
      self.root.printLevel(level)
      return str()
    
  def getHeight(self):
      if self.root == None:
          return 0
      #Although the root is on level 1, the height starts at 0 
      return self.root.getHeight(height=0)

  def getNodes_left(self):
      return self.root.getNodes_left()
      
  def getNodes_right(self):
      return self.root.getNodes_right()
 
def main():
    
    #create two trees and insert the values into each tree
    t1 = Tree()
    a = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    t1.insert_val(a)
    t3 = Tree()
    b = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    t3.insert_val(b)
    t2= Tree()
    
    '''isSimilar Test'''
    print(t1.isSimilar(t2))

    '''printLevel test'''
    print(t1.printLevel(3))

    '''getHeight test'''
    print(t1.getHeight())

    '''numNodes test'''
    t1_l = t1.getNodes_left()
    t1_r = t1.getNodes_right()
    
    #print number of nodes on left and right subtrees separately
    print("Left Nodes:",t1_l)
    print("Right Nodes:",t1_r)
    
main()
        
    


