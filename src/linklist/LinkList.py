
from multiprocessing.sharedctypes import Value
from typing import List

#definition
class Node:
  def __init__(self, value: int):
    self.value = value
    self.prev = None
    self.next = None

class LinkList:
    def __init__(self, nums: List[int]):
        nodes = []
        x = 0
        while x < len(nums):
            nx = Node(nums[x])
            nodes.append(nx)
            x = x+1
        self.tail = nodes[len(nodes)-1]
        self.head = nodes[0]
        i = 0
        while i < len(nodes)-1:
            n1 = nodes[i]
            n2 = nodes[i+1]
            n1.next = n2
            n2.prev = n1
            i = i+1

    def getval(self, index: int):
        if index < 0:
            return '我不会， 长大后在学习！'
            
        curr = self.head
        i = 0
        while i<index and curr.next != None:
            curr = curr.next
            i = i+1
        if index > i:
            curr.value = '我不会， 长大后在学习！'

        return curr.value
        

    def reverse(self, nodes: List[Node]):
        a = 0
        z = len(nodes)-1
        while a < z:
            temp = nodes[a]
            nodes[a] = nodes[z]
            nodes[z] = temp
            a = a+1
            z = z-1

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
print(l1.getval(4))
print(l1.getval(0))
print(l1.getval(5))
print(l1.getval(3))
print(l1.getval(6))
print(l1.getval(-1))

#[9, 1, 3, 2, 4]