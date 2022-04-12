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
    print( 'Hello!  I am a list.  My head is', self.head.value, ', my tail is', self.tail.value)

# execution
p1 = Node(4, None, None)
p2 = Node(2, p1, None)
p1.next = p2
p1.print()
p2.print()

l1= LinkList(p1, p2)
l1.print()
# l1.print() # 4 -> 2
