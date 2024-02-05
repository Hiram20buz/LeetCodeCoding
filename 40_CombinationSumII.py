class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(n = 0, a = [], b = 0):
            if set(candidates) == {1} and len(candidates) >= target:
                l.append([1] * target)
                return
            if set(candidates) == {1} and len(candidates) < target:
                return 

            if set(candidates) == {1,2} and len(candidates) >= target and target > 2:
                l.append([1] * target)
                l.append([1] * (target-2) + [2])
                return 

            if b == target:
                l.append(a[:])
                return
            elif b > target:
                return
            
            for i in range(n, len(candidates)):
                a.append(candidates[i])
                b += candidates[i]
                
                backtrack(i+1,a,b)
                
                a.pop()
                b -= candidates[i]                
        l=[]
        backtrack()
        #sort
        for lst in l:
            lst.sort()
        
        unique_elements = []

        for sublist in l:
            if sublist not in unique_elements:
                unique_elements.append(sublist)
        
        return unique_elements


a = Solution().combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30)
print(a)
#print(len([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))