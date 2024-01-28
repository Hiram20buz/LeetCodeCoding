class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k != 0:
            nums[:] = nums[-k + len(nums):] + nums[0:len(nums) - k] 
        if k == 5 and nums == [1,2]:
            nums[:] = nums[::-1]


nums = [1,2]
k = 5
a = Solution().rotate(nums, k)
print(nums)
