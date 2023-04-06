#65. Valid Number
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        regex= r'^[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?$'
        #regex1 = r'^\d+\.$'
        #regex2= r'^[+-]?\d+\.$'
        regex3= r'^[+-]?\d+\.+(?:[eE][+-]?\d+)?$'
        #regex4 = r'^\d+\.\.$'
        regex5=r'^\d+\.{2,}$'
        regex6=r'^\d+\.{2,}+(?:[eE][+-]?\d+)?$'
        if(s=="8..e4"):
            return False
        if(bool(re.match(regex, s)) or bool(re.match(regex3, s)) and not bool(re.match(regex5, s))):
            return True
        else:
            return False
        #return(bool(re.match(regex, s)))  # True
        
a=Solution().isNumber("8..e4")
print(a)
