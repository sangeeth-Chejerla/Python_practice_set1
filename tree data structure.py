class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Height:
    def __init__(self):
        self.h = 0

def diameter_of_tree(root,height):
    lh = Height()
    rh = Height()
    if root is None:
        height.h = 0
        return 0
    ldiameter = diameter_of_tree(root.left,lh)
    rdiameter = diameter_of_tree(root.right,rh)

    height.h = max(lh.h,rh.h)+1
    return max(lh.h + rh.h,max(ldiameter,rdiameter))

def diameter(root):
    height = Height()
    return diameter_of_tree(root,height)

root = Node(1)

root.left= Node(2)
root.right =Node(3)
root.left.left = Node(4)
print(diameter(root))