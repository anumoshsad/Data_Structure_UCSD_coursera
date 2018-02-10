# python3

import sys

#splay tree implementation

#vertex of a splay tree
class Vertex:
  def __init__(self, key, size, left, right, parent):
    (self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)


def update(v):
  if v == None:
    return
  v.size = 1 + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
# def find(root, key): 
#   v = root
#   last = root
#   next = None
#   while v != None:
#     if v.key >= key and (next == None or v.key < next.key):
#       next = v    
#     last = v
#     if v.key == key:
#       break    
#     if v.key < key:
#       v = v.right
#     else: 
#       v = v.left
#   root = splay(last)
#   return (next, root)
def orderStatistics(root, k):
  s = 0
  if root.left != None:
    s = root.left.size
  if k == s + 1:
    return root
  elif k < s+1:
    return orderStatistics(root.left, k)
  elif k > s+1:
    return orderStatistics(root.right, k - s - 1)

def split(root, k):
  if root == None: return (None, None)
  if root !=None and k<=0 : return (None, splay(orderStatistics(root, 1)))
  if root !=None and k>root.size: return (splay(orderStatistics(root, root.size)), None)
  node = orderStatistics(root, k)  
  right = splay(node)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right



# Code that uses splay tree to solve the problem
def inOrder(node):
  s = []
  while s or node!= None:
    if node != None: 
      s.append(node)
      node = node.left
    else:
      node = s.pop()
      print(node.key, end = '')
      node = node.right
  print("\n", end ="")


root = None

def insert(char):
  global root
  new_vertex = Vertex(char, 1 , None, None, None)  
  root = merge(root, new_vertex)




class Rope:
  def __init__(self, s):
    global root
    self.s = s
    for x in range(len(self.s)):
      insert(s[x])

  def result( self ):
    global root
    inOrder(root)

  def process(self, i, j, k):
    global root
    (middle, right) = split(root, j+2)
    
    (left, middle) = split(middle, i+1)
    
    root = merge(left, right)
    (left, right) = split(root, k+1)
    #print("rootSize =", root.size, end ="");inOrder(root)
    #inOrder(left); inOrder(middle);inOrder(right);print(i,j, k )
    
    root = merge(left, merge(middle, right))
    #inOrder(root)
  


                

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
  i, j, k = map(int, sys.stdin.readline().strip().split())
  for k in range(6):
    rope.process(i, j, k)
    print(i,j,k); rope.result()
