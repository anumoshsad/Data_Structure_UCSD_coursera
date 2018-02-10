# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                height = [-1 for i in range(self.n)]
                for i in range(self.n):
                    if self.parent[i] == -1:
                        height[i] = 0
        
                
                
                for vertex in range(self.n):
                        parent_vertex = self.parent[vertex]
                        i = vertex
                        h = 0
                        while height[i] == -1:
                                h += 1
                                i = self.parent[i]
                        j = vertex
                        #print(i, h)
                        while j!=i:
                            height[j] = h + height[i]
                            j = self.parent[j]
                            h -= 1
                        #print(height)
                        
                return max(height)+1;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
