# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
         
class ListNode:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
         
    def printl(self):
        n = self.head
        val=[]
        while n:
            val.append(n.data)
            n = n.next
        #print()
        return val
 
 
class Solution:
    def addTwoNumbers(self,l1: ListNode, l2: ListNode):
        num1, num2 = 0, 0
        while first.head:
            num1 = num1*10 + first.head.data
            first.head = first.head.next
        while second.head:
            num2 = num2*10 + second.head.data
            second.head = second.head.next
        num3 = num1 + num2
        temp = ListNode()
        while num3:
            last = num3 % 10
            temp.push(last)
            num3 = num3 // 10
        return temp
 
if __name__ == '__main__':
    first = ListNode()
    second = ListNode()
    first.push(9)
    first.push(9)
    first.push(9)
    first.push(9)
    first.push(9)
    first.push(9)
    first.push(9)

    print(first.printl())
 
    second.push(9)
    second.push(9)
    second.push(9)
    second.push(9)
    print(second.printl())
    
    ans=Solution().addTwoNumbers(first,second)
    print(ans.printl())
 
    
 
  
