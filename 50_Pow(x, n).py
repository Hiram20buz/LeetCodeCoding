#50. Pow(x, n)
from decimal import Decimal
x =  Decimal('2.00000')
n = -2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        y =pow(x, n)
        
        decix=len(str(x))-len(str(int(x)))-1
        #print(decix)
        
        deciy=len(str(y))-len(str(int(y)))-1
        #print(deciy)
        #print(y)
        
        num=list(str(y))
        #print(num)
        if(deciy-decix > 0):
            for val in range(deciy-decix):
                num.pop()
                
        if(deciy-decix < 0):
            #print(1)
            for val in range(decix-deciy):
                #print(deciy-decix)
                num.append("0")
              
        str1 = ""       
        for ele in num:
            str1 += ele
        return(Decimal(str1))
             
a=Solution().myPow(x,n)
print(a)
