class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            deleted_item = nums.pop(0)
            if deleted_item not in nums:
                return deleted_item
            nums.append(deleted_item)


a = Solution().singleNumber([1,2,1,2,4])
print(a)