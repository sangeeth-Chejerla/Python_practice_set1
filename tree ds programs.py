class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

"""inorder traversal in the tree it moves along the tree and reaches all the nodes.
    left
    root
    right 
    """
def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data,end ="-")
    inorder(temp.right)

def insertion(temp,data):
    if not temp:
        root = temp(data)
        return
    q= []
    q.append(temp)
    while len(q):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print("Inorder traversal before insertion:", end=" ")
inorder(root)

key = 12
insertion(root, key)

print()
print("Inorder traversal after insertion:", end=" ")
inorder(root)




