class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]

        return len(nums)


nums = [3,2,2,3]
a = Solution().removeElement(nums, 3)
print(a)
'''
nums = [1, 2, 3, 4, 5, 3, 6, 7, 3]
val = 3

# Using a for loop to remove elements
for x in nums[:]:  # Iterating over a copy of nums to avoid issues with modifying it while iterating
    if x == val:
        nums.remove(x)

print(nums)  # Output: [1, 2, 4, 5, 6, 7]
'''

'''
# Using a loop to remove elements
i = 0
while i < len(nums):
    if nums[i] == val:
        del nums[i]
    else:
        i += 1

print(nums)  # Output: [1, 2, 4, 5, 6, 7]
'''