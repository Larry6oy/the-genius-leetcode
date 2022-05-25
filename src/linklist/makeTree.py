class Node:
    def makeNode(self, left, right):
        self.left = self.left
        self.right = self.right
class Tree:
    def makeTree(self, left, right):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n1.left = n2
        n1.right = n3
        t = Tree(n1)
        return t