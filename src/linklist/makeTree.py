from ast import Global


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self, value: Node):
        self.root = value
    def toString(self):
        r = '('
        r = r+'1, '
        r = r+'2, '
        r = r+'3'
        r = r+')'
        return r
    def print(self):
        string = []
        p = self.root
        q = self.root
        while p != None and q != None:
            if q != p:
                string.append(str(p.value))
                string.append(str(q.value))
                p = p.left
                q = q.right
            else:
                string.append(str(p.value))
                p = p.left
                q = q.right
        ', '.join(string)
        return string.value


def makeTree():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = None
    t = Tree(n1)
    return t

def makeSimpleTree():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.left = n2
    n1.right = n3
    tr = Tree(n1)
    return tr
t = makeSimpleTree()
print(t.toString())
#print(makeTree())
print(t)