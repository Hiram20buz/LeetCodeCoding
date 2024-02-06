from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        num2freq = defaultdict(int)
        n = len(nums)
        out = []
        for num in nums:
            num2freq[num]+=1

        def backtrack(seq, hashMap):
            if len(seq) == 2:
                out.append(seq[:])
                return

            for num in hashMap:
                if hashMap[num]>0:
                    seq.append(num)
                    hashMap[num]-=1

                    backtrack(seq, hashMap)

                    seq.pop()
                    hashMap[num]+=1

        backtrack([], num2freq)
        for lst in out:
            lst.sort()
        #return out
        unique_elements = []

        for sublist in out:
            if sublist not in unique_elements:
                unique_elements.append(sublist)
        
        return unique_elements

        
print(Solution().permuteUnique([1,2,3,4]))