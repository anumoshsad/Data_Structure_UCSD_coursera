# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self._n = 0

  def ReadData(self):
    self._n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self._n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    #print(self._data)
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    #for i in range(len(self._data)):
    # for j in range(i + 1, len(self._data)):
    #   if self._data[i] > self._data[j]:
    #     self._swaps.append((i, j))
    #     self._data[i], self._data[j] = self._data[j], self._data[i]
    def parent(i):
        return (i-1)//2
    def leftChild(i):
        return 2*i + 1
    def rightChild(i):
        return 2*i + 2
    def siftDown(i):
        minIndex = i
        l = leftChild(i)
        if l<= self._n-1 and self._data[l] < self._data[minIndex]:
            minIndex = l
        r = rightChild(i)
        if r<= self._n-1 and self._data[r] < self._data[minIndex]:
            minIndex = r
        if i != minIndex:
            #print(i, minIndex,"hi")
            self._swaps.append((i,minIndex))
            temp = self._data[i]
            self._data[i] = self._data[minIndex]
            self._data[minIndex] = temp
            siftDown(minIndex)


    for i in range(self._n//2-1,-1,-1):
        siftDown(i)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
