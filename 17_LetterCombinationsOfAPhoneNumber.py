#17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
a=Solution().letterCombinations("")
print(a)

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
#print(thisdict)
def a(s):
    num=list(s)
    #print(num)
    if(s==""):
        print("")
    if(len(num)==1):
        print(thisdict[int(num[0])])
        
    if(len(num)==2):
        list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
        print(list2)
        
    if(len(num)==3):
        list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
        list3 = [f'{a}{b}' for a in list2 for b in thisdict[int(num[2])]]
        print(list3)
        
    if(len(num)==4):
        list2 = [f'{a}{b}' for a in thisdict[int(num[0])] for b in thisdict[int(num[1])]]
        list3 = [f'{a}{b}' for a in list2 for b in thisdict[int(num[2])]]
        list4 = [f'{a}{b}' for a in list3 for b in thisdict[int(num[3])]]
        print(list4)
    
a("")
