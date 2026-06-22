af
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

ans = -1
def height(root):
    global ans
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    ans = max(ans, left_height + right_height)
    return 1 + max(left_height, right_height)

def diameter(root):
    global ans
    if root is None:
        return 0
    # ans = [-1]  # Using a list to emulate passing by reference
    height(root)
    return ans


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left= Node(6)
    print(diameter(root))

if __name__ == "__main__":
    main()

