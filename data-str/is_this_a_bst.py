""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
a = []
def halo(root):
    if root:
        halo(root.left)
        a.append(root.data)
        halo(root.right)

def checkSort(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1] or a[i] == a[i+1]:
            return False
    return True

def checkBST(root):
    halo(root)
    return checkSort(a)
