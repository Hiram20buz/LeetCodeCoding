class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move the first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move first to the end, maintaining the gap between first and second
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        return remove_nth_from_end(head, n)

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

a = Solution().removeNthFromEnd(linked_list, 2)
# Print the updated linked list
while a:
    print(a.val, end=" ")
    a = a.next