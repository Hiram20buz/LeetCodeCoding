#50. Pow(x, n)
from decimal import Decimal
'''
num = 2.00000
formatted_num = "{:.5f}".format(num)
#print(formatted_num)
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = "{:.5f}".format(x)
        
            
        
            
        y =pow(x, n)
        
        print(y)
        dis=len(str(num).split(".")[1])
        print(dis)
        
        dis1=len(str(y).split(".")[1])
        print(dis1)
        
        num=list(str(y))
        
        if(dis-dis1 > 0):
            for val in range(dis-dis1):
                num.append("0")
                
                
        if(dis-dis1 < 0):
            #print(1)
            for val in range(dis1-dis):
                #print(deciy-decix)
                num.pop()
        
              
        str1 = ""       
        for ele in num:
            str1 += ele
            
        
         
        #return numx   
        #return(Decimal(str1))
        #return(float(str1))
        #return round(Decimal(str1))
        return y

             
a=Solution().myPow(23.56502,-3)
print(a)





