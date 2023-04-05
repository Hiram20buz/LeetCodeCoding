class Solution():
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        
a=Solution().isPalindrome(-121)
print(a)
