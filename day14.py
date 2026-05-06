class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
        
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.right.right=Node(8)
    inorder(root)

if __name__ == "__main__":
    main()
