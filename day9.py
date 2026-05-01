
class Node:
    def __init__(self, value=0, next_node=None):
        self.data = value
        self.next = next_node


def LengthOfCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0


def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        cur.next = Node(value)
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def convert_to_cycle(head, k):
    temp = head
    count = 0
    end_node = None
    while temp:
        if count == k:
            end_node = temp
            break
        count += 1
        temp = temp.next
    if not end_node:
        return head
    if temp:
        while temp.next:
            temp = temp.next
        temp.next = end_node
    return head

n = int(input())
arr = list(map(int, input().split()))
cycleStartingPoint = n//2 # If a cycle exists, this variable serves as the starting point. If not, its value will be greater than n.
head = array_to_LL(arr)
head = convert_to_cycle(head, cycleStartingPoint)
print(LengthOfCycle(head))
