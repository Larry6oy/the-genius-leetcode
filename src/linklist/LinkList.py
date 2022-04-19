
from typing import List

#definition
class Node:
  def __init__(self, value: int, prev, next):
    self.value = value
    self.prev = prev
    self.next = next

  def print(self):
    print("Hello my value is", self.value)

class LinkList:
  def __init__(self, head: Node, tail: Node):
    self.tail = tail
    self.head = head

  def print(self):

    p = self.head
    strs = [ ]
    while p != None:
        strs.append(str(p.value))
        p = p.next
        
    print( 'Hello!  I am a list.  My values are', ' -> '.join(strs))

# execution
p1 = Node(4, None, None)
p2 = Node(2, p1, None)
p3 = Node(3, p2, None)
p4 = Node(1, p3, None)
p5 = Node(9, p4, None)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5


p1.print()
p2.print()
l1= LinkList(p1, p5)
l1.print()
# l1.print() # 4 -> 2
