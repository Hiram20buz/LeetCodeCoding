class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linked_list = ListNode(1, ListNode(2, ListNode(4)))
linked_list1 = ListNode(1, ListNode(3, ListNode(4)))

#a = Solution().removeNthFromEnd(linked_list, 2)
# Print the updated linked list
while linked_list1:
    print(linked_list1.val, end=" ")
    linked_list1 = linked_list1.next