class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def height(root, ans):
    if root is None:
        return 0
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)
    diff = abs(left_height - right_height)
    if diff > 1:
        ans[0] = False
    return 1 + max(left_height, right_height)

def balanced(root):
    ans = [True]
    height(root, ans)
    return ans[0]


def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.right.left = Node(50)
    root.right.right = Node(60)
    res=balanced(root)
    if(res==True):
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    main()
