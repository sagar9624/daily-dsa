class Node:
    def __init__(self, value, address=None):
        self.data = value
        self.next = address

"""
def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        temp = Node(value)
        cur.next = temp
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
"""

def sortLL0s1s2s(head):
    temp = head
    prev_0 = prev_1 = prev_2 = None
    first_0 = first_1 = first_2 = None
    while temp:
        if temp.data == 0:
            if prev_0 is None:
                first_0 = temp
            else:
                prev_0.next = temp
            prev_0 = temp
        elif temp.data == 1:
            if prev_1 is None:
                first_1 = temp
            else:
                prev_1.next = temp
            prev_1 = temp
        elif temp.data == 2:
            if prev_2 is None:
                first_2 = temp
            else:
                prev_2.next = temp
            prev_2 = temp
        temp = temp.next

    if prev_0:
        if first_1:
            prev_0.next = first_1
        else:
            prev_0.next = first_2
    if prev_1:
        prev_1.next = first_2
    if prev_2:
        prev_2.next = None

    if first_0:
        return first_0
    if first_1:
        return first_1
    return first_2

"""
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = sortLL0s1s2s(head)
    print_LL(head)
"""
