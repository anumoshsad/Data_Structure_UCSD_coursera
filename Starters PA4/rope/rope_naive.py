#python 3

import sys

string = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
for _ in range(q):
  	i, j, k = map(int, sys.stdin.readline().strip().split())
  	left = string[0:i]
  	middle= string[i:j+1]
  	right = string[j+1:]
  	new = left + right
  	string = new[:k] + middle + new[k:]
  	
print(string)