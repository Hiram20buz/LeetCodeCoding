class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        nums.append(target)
        nums.sort()
        return self.searchInsert(nums, target)
   


# Example usage:
arr = [1,3,5,6]
target = 7
a = Solution().searchInsert(arr, target)
print(a)
print(arr)