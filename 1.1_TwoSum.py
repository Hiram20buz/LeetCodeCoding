class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        indices = []
        double = 0
        for num in nums:
            if ((target - num in seen) and (num == target - num)):
                double = num
            elif ((target - num in seen) and (num != target - num)):
                indices.append(nums.index(num))
                indices.append(nums.index(target - num))
                return indices
            seen[num] = True
        if not indices:
            return [index for index, value in enumerate(nums) if value == double]
       
a = Solution().twoSum([3, 3], 6)

print(a)
