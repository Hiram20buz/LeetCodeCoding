class Solution(object):
    ###
    ###Palidrome
    def isPalindrome(self,a):
        return a == a[::-1]
            
         
         
    def longestPalindrome(self,s) :
        res = [s[i: j] for i in range(len(s))
              for j in range(i + 1, len(s) + 1)]
        pal = {}
        
        #print(a_dict)
        for palabra in res:
            if(self.isPalindrome(palabra)==1):
               # pal.append(len(palabra))
               pal[palabra] = len(palabra)
        #print(pal)       
        #print(max(pal.values()))
        
        for val in pal:
            if(pal[val]==max(pal.values())):
                return val
                
   
   

w=Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
print(w)  
