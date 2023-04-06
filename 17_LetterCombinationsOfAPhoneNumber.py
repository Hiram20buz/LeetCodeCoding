#17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        thisdict = {
          2: ["a", "b", "c"],
          3: ["d", "e", "f"],
          4: ["g", "h", "i"],
          5: ["j", "k", "l"],
          6: ["m", "n", "o"],
          7: ["p", "q", "r","s"],
          8: ["t","u", "v"],
          9: ["w", "x", "y","z"],
        }
        num=list(digits)
        #print(num)
        if(digits==""):
            return([])
            
        if(len(num)==1):
            return(thisdict[int(num[0])])
            
        if(len(num)==2):
            list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
            return(list2)
            
        if(len(num)==3):
            list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
            list3 = [f'{a}{b}' for a in list2 for b in thisdict[int(num[2])]]
            return(list3)
            
        if(len(num)==4):
            list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
            list3 = [f'{a}{b}' for a in list2 for b in thisdict[int(num[2])]]
            list4 = [f'{a}{b}' for a in list3 for b in thisdict[int(num[3])]]
            return(list4)
        
        
a=Solution().letterCombinations("")

print(a)

