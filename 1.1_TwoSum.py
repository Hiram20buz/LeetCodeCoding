class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        indices = []
        for num in nums:
            if target - num in seen:
                indices.append(nums.index(num))
                indices.append(nums.index(target - num))
                break
            seen[num] = True

        return indices
       
a = Solution().twoSum([2,7,11,15], 9)
print(a)
