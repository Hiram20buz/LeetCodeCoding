# Regular Expression Matching
# Importing re module
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #return re.fullmatch(p,s)
        return True if re.fullmatch(p,s) else False
        
a=Solution().isMatch("aa","a*")
print(a)

'''
pattern="a*"

s= "aa"
		
if(re.fullmatch(pattern,s)):
    print("**Match found** ")
else:
    print("Match not found ") 
'''
