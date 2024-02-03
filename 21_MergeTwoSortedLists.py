class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_sort(self, head):
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        mid = self.get_middle(head)
        next_to_mid = mid.next
        mid.next = None

        # Recursively sort both halves
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
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

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        list1 = self.merge_sort(list1)
        list2 = self.merge_sort(list2)
        
        # Iterate through both lists
        while list1 and list2:
            # Compare values of nodes and append the smaller one
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes if any
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next

# Example usage
# Create two sorted linked lists
l1 = ListNode(1, ListNode(1, ListNode(4)))
l2 = ListNode(9, ListNode(8, ListNode(4)))

# Merge the two lists
merged_list = Solution().mergeTwoLists(l1, l2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
