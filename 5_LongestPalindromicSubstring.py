class Solution(object):
    ###
    ###Substrings
    def substrings(self,test_str):
        res = [test_str[i: j] for i in range(len(test_str))
              for j in range(i + 1, len(test_str) + 1)]
              
        return res
    
      
    
    #print(substrings("babad"))
    
    ###
    ###Palidrome
    def isPalindrome(self,a):
        b=list(a)
        c=[]
        for i in range(len(b)):
            c.append(b[len(b)-1-i])
            
        if(b==c):
            return 1
        else:
            return -1
            
         
         
    def longestPalindrome(self,s) :
        pal = {}
        
        #print(a_dict)
        for palabra in self.substrings(s):
            if(self.isPalindrome(palabra)==1):
               # pal.append(len(palabra))
               pal[palabra] = len(palabra)
        #print(pal)       
        #print(max(pal.values()))
        
        for val in pal:
            if(pal[val]==max(pal.values())):
                return val
                
   
   

w=Solution().longestPalindrome("babad")
print(w)  
