class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.val
        self.val = new_node
         
    def printl(self):
        n = self.val
        val=[]
        while n:
            val.append(n.val)
            n = n.next
        #print()
        return val
 
 
class Solution:
    def addTwoNumbers(self,l1: ListNode, l2: ListNode):
        num1, num2 = 0, 0
        while first.val:
            num1 = num1*10 + first.val.val
            first.val = first.val.next
        while second.val:
            num2 = num2*10 + second.val.val
            second.val = second.val.next
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
