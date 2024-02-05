class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(n = 0, a = [], b = 0):
            if b == target:
                l.append(a[:])
                return
            elif b > target:
                return
            
            for i in range(n, len(candidates)):
                a.append(candidates[i])
                b += candidates[i]
                
                backtrack(i,a,b)
                
                a.pop()
                b -= candidates[i]                
        l=[]
        backtrack()
        return l


a = Solution().combinationSum([2,3,5], 8)
print(a)