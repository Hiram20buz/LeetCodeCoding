
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

        
result = ListNode(0)
#result = 0 -> None
result_tail = result
#result_tail = 0 -> None
result_tail.next = ListNode(1)
#result_tail = 0 -> 1 -> None
#result = 0 -> 1 -> None
result_tail = result_tail.next
#result_tail = 1 -> None
#result = 0 -> 1 -> None
result_tail.next = ListNode(2)
#result_tail = 1 -> 2 -> None
#result = 0 -> 1 -> 2 -> None
result_tail = result_tail.next
#result_tail = 2 -> None
#result = 0 -> 1 -> 2 -> None

print(result_tail)

https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode
