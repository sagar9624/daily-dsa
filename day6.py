class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

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

def reverse_LL(head):
    cur = head
    prev = None
    front = None
    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front
    return prev

def add1ToLL(head):
    head = reverse_LL(head)
    temp = head
    carry = 1
    while temp:
        _sum = temp.data + carry
        temp.data = _sum % 10
        carry = _sum // 10
        if carry == 0:
            break
        temp = temp.next
    head = reverse_LL(head)
    if carry == 1:
        new_node = Node(1, head)
        head = new_node
    return head


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = add1ToLL(head)
    print_LL(head)
