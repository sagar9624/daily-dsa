class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

"""
def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        cur.next = temp
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
"""

def delete_middle_node(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    del slow
    return head

"""
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = delete_middle_node(head)
    print_LL(head)
"""
