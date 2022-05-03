
from typing import List

#definition
class Node:
  def __init__(self, value: int):
    self.value = value
    self.prev = None
    self.next = None

  def print(self):
    print("Hello my value is", self.value)

class LinkList:
    def __init__(self, nums: List[int]):
        nodes = []
        x = 0
        while x < len(nums)-1:
            nx = Node(nums[x])
            nodes.append(nx)
            x = x+1
        self.___init__(nodes)

    def ___init__(self, nodes: List[Node]):
        self.tail = nodes[len(nodes)-1]
        self.head = nodes[0]
        i = 0
        while i < len(nodes):
            n1 = nodes[i]
            n2 = nodes[i+1]
            n1.next = n2
            n2.prev = n1
            i = i+1

    def print(self):
        p = self.head
        strs = [ ]
        while p != None:
            strs.append(str(p.value))
            p = p.next
        
        print( 'Hello!  I am a list.  My values are', ' -> '.join(strs))

# execution
p1 = Node(4)
p2 = Node(2)
p3 = Node(3)
p4 = Node(1)
p5 = Node(9)



#l1= LinkList([p1, p2, p3, p4, p5])
l1 = LinkList([4, 2, 3, 1, 9])
l1.print()
# l1.print() # 4 -> 2
