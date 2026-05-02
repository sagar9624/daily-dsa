'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
'''
        
class solution:
    def doubleLinkedList(self, Node, head):
        curr = head
        prev = None

        while curr:
            double_value = curr.data * 2

            if double_value < 10:
                curr.data = double_value
            else:
                curr.data = double_value % 10
                carry = double_value // 10

                if prev:
                    prev.data += carry
                else:
                    new_head = Node(carry)
                    new_head.next = head
                    head = new_head
                    prev = new_head

            prev = curr
            curr = curr.next

        return head
