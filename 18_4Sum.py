class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        lst = []
        # Sort the array in increasing order, 
        # using library function for quick sort
        nums.sort()

        # Now fix the first 2 elements one by 
        # one and find the other two elements 
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                # Initialize two variables as indexes 
                # of the first and last elements in 
                # the remaining elements
                l = j + 1
                r = n - 1

                # To find the remaining two elements, 
                # move the index variables (l & r)
                # toward each other.
                while (l < r):
                    if(nums[i] + nums[j] + nums[l] + nums[r] == target):
                        lst.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    
                    elif (nums[i] + nums[j] + nums[l] + nums[r] < target):
                        l += 1
                    else:
                        r -= 1
        
        unique_set = set()
        result = []
        for sublist in lst:
            # Convert the sublist to a tuple because lists are unhashable and cannot be stored in a set
            sublist_tuple = tuple(sublist)
            if sublist_tuple not in unique_set:
                unique_set.add(sublist_tuple)
                result.append(sublist)

        return result
        

c = Solution().fourSum([2,2,2,2,2], 8)
print(c)