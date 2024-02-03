class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None

    # Recursively sort both halves
    left = merge_sort(head)
    right = merge_sort(next_to_mid)

    # Merge the sorted halves
    return merge(left, right)

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next

# Example usage
linked_list = ListNode(1, ListNode(5, ListNode(4)))
sorted_list = merge_sort(linked_list)

# Print the sorted linked list
while sorted_list:
    print(sorted_list.val, end=" ")
    sorted_list = sorted_list.next
