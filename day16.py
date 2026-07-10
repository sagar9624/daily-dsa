
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return []
    
    queue = [root]
    ans = []
    
    while queue:
        length = len(queue)
        for i in range(length):
            temp = queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            ans.append(temp.data)
    
    return ans

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    res=levelOrder(root)
    for i in res:
        print(i,end=' ')

if __name__ == "__main__":
    main()
