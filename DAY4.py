#Linear search in python
def linearSearch(array, n, x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1

array = [2,4,0,1,9]
x = 1 #input
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:", result)
    

#Binary search in python
def binarySearch(array, x, low, high):
    while low<=high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present in index :" + str(result))
else:
    print("Element not found")

#A python class that represent an indivisual node in binary tree
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val= item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->",end=' ')
def preorder(root):
    if root:
        print (str(root.val)+ "->", end= ' ')
        preorder (root.left)
        preorder (root.right)
root=Node(1)
root.left=Node(2) 
root.right = Node (3) 
root.left.left=Node(4)
root.left.right=Node(5)
print ("Inorder traversal ")
inorder(root)
print ("\npreorder traversal ")
preorder(root)
print ("\nposterder traversal ")
postorder(root)


#binary search tree norder traversal
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        return node
def minvaluenode(node):
    current=node
    while(current.left is not None):
        current = current.left
    return current
def deletenode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deletenode(root.left,key)
    elif(key > root.key):
        root.right = deletenode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root=None
            return temp
        temp = minvaluenode(root.right)
        root.key = temp.key
        root.right = deletenode(root.right,temp.key)
    return root
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14) 
root = insert(root, 4)
print("Inorder trversal:", end=' ')
inorder(root)
print("\n Delete 10")
