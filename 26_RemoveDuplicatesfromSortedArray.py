class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))

        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
a = Solution().removeDuplicates(nums)
print(a)
