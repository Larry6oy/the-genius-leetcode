
from email import header
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
    

    def swap(self, p1: Node, p2: Node):
        p1n = p1.next
        p1p = p1.prev
        p2n = p2.next
        p2p = p2.next
        if p1n == p2:
            p1.prev = p2
            p2.next = p1
            p1.next = p2n
            p2.prev = p1p
        elif p1p == p2:
            p1.next = p2
            p2.prev = p1
            p1.prev = p2p
            p2.next = p1n
        else:
            p1.prev = p2p
            p2.next = p1n
            p1.next = p2n
            p2.prev = p1p

        if self.head == p1:
            self.head = p2
        elif self.head == p2:
            self.head = p1
        if self.tail == p2:
            self.tail = p1
        elif self.tail == p1:
            self.tail = p2
        

    def reverse(self):
        p = self.head
        r = self.tail
        #print(r.value)
        while r.next != p and r != p:
            self.swap(p, r)
            temp = p
            p = r
            r = temp
            #self.print()
            print(p.value, r.value)
            p = p.next
            r = r.prev
            print(p.value, r.value)


    def print(self):
        p = self.head
        strs = [ ]
        while p != None:
            strs.append(str(p.value))
            p = p.next
        
        print( 'Hello!  I am a list.  My values are', ' -> '.join(strs))

# execution
#p1 = Node(4)
#p2 = Node(2)
#p3 = Node(3)
#p4 = Node(1)
#p5 = Node(9)
pp1 = Node(1)
pp2 = Node(3)
pp3 = Node(2)



#l1= LinkList([p1, p2, p3, p4, p5])
l1 = LinkList([1, 3, 2])
l1.print()
#print(l1.getval(4))
#print(l1.getval(0))
#print(l1.getval(5))
#print(l1.getval(3))
#print(l1.getval(6))
#print(l1.getval(-1))
#l1.reverse()
l1.swap(l1.head, l1.tail)
#l1.reverse()
l1.print()

#[9, 1, 3, 2, 4]