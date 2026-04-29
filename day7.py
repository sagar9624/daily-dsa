class Node:
    def __init__(self, value=0, next=None):
        self.data = value
        self.next = next

def intersectionOfTwoLL(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next
        if temp1 == temp2:
            return temp1
        if temp1 == None:
            temp1 = head2
        if temp2 == None:
            temp2 = head1
    return temp1


def create_linked_list(values):
    #Create a linked list from a list of values.
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def find_common_subarray(arr1, arr2):
    #Identify the longest common subarray at the end of both arrays.
    i, j = len(arr1) - 1, len(arr2) - 1
    common = []
    # Start from the end and move backward as long as elements are equal
    while i >= 0 and j >= 0 and arr1[i] == arr2[j]:
        # Prepend the common element to the common list
        common.insert(0, arr1[i])
        i -= 1
        j -= 1
    return arr1[:i+1], arr2[:j+1], common  # Return unique parts and common subarray

def append_common_part(unique_head, common_head):
    
    #Appends the common part of the list to the end of the unique part.
    #If the unique part is None, return the common part directly.
    
    if not unique_head:  # If the unique part is empty, return the common part
        return common_head
    current = unique_head
    while current.next:  # Traverse to the end of the unique part
        current = current.next
    current.next = common_head  # Append the common part
    return unique_head

def print_linked_list(head):
    #Print the linked list.
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Given input arrays
m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Find the common subarray and the unique parts
unique1, unique2, common = find_common_subarray(arr1, arr2)

# Create the common part of the linked lists
common_list = create_linked_list(common)

# Create the full lists including their unique parts
list1 = append_common_part(create_linked_list(unique1), common_list)
list2 = append_common_part(create_linked_list(unique2), common_list)

print_linked_list(intersectionOfTwoLL(list1, list2))
