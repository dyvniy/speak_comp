#t2
# treeorder.py
import sys
def print0(s):
    sys.stdout.write(s)
def isOp(s):
    return s in ['+', '-', '*', '/']
class Tree:
    left = None
    right = None
    data = None
    def __init__(self, data0=None, left0=None, right0=None):
        if not data0 is None:
            self.root = self
            self.data = data0
            if not left0 is None:
                self.left = left0
            if not right0 is None:
                self.right = right0
    def print(self, tree, i=0):
        if tree.data is None:
            print(None)
        else:
            print(str(i) + ' ' + str(tree.data))
            if not tree.left is None:
                self.print(tree.left, i+1)
            if not tree.right is None:
                self.print(tree.right, i+1)
    def parse(self, s):
        arr = []
        for a in s:
            arr.append(a)
        return self.treeA(arr, len(arr))
    def balansed(self, n):
        newnode = None
        if n > 0:
            nl = n // 2
            nr = n - nl - 1
            newnode = Tree(n)
            newnode.left = self.balansed(nl)
            newnode.right = self.balansed(nr)
        return newnode
    def balansedA(self, arr, n):
        newnode = None
        if n > 0:
            nL = n // 2
            nR = n - nL - 1
            newnode = Tree(arr.pop(0))
            newnode.left = self.balansedA(arr, nL)
            newnode.right = self.balansedA(arr, nR)
        return newnode
    def preo(self, t):
        if not t is None:
            print0(t.data+' ')
            self.preo(t.left)
            self.preo(t.right)
    def inor (self, t):
        if not t is None:
            d = t.data
            f = isOp(d)
            if f: print0('(')
            self.inor(t.left)
            print0(d)
            self.inor(t.right)
            if f: print0(')')
    def psto(self, t):
        if not t is None:
            self.psto(t.left)
            self.psto(t.right)
            print0(t.data+' ')
def makeTree():
    t = Tree('*')
    t.left = Tree('+')
    t.right = Tree('-')
    t.left.left = Tree('a')
    t.left.right = Tree('/')
    t.left.right.left = Tree('b')
    t.left.right.right = Tree('c')
    t.right.left = Tree('d')
    t.right.right = Tree('*')
    t.right.right.left = Tree('e')
    t.right.right.right = Tree('f')
    return t
#t = t.parse('*+a/bc-d*ef')
#'(a+b/c)*(d - e*f)')
ar = [1, 2, 3, 4, 5, 6]
#t = t.balansedA(ar[:], len(ar))
t = makeTree()
t.print(t)
print('\n preorder')
t.preo(t)
print('\n inorder')
t.inor(t)
print('\n postorder')
t.psto(t)
