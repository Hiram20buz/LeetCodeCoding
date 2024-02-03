class Solution:
    # Python code to implement the above approach
    def swapPositions(self, lst, pos1, pos2):
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst
    
    # Function to find the next permutation
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = len(nums)-2
        j = 0
        
        # Find for the pivot element.
        # A pivot is the first element from
        # end of sequencewhich doesn't follow
        # property of non-increasing suffix
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i=i-1
                
        # Check if pivot is not found
        if (i < 0):
            nums.reverse()
    
        # if pivot is found
        else:
            # Find for the successor of pivot in suffix
            for j in range(n-1, i, -1):
                if (nums[j] > nums[i]):
                    break
    
            # Swap the pivot and successor
            self.swapPositions(nums, i, j)
            
            # Minimise the suffix part
            # initializing range
            strt, end = i+1, len(nums)
    
            # Third arg. of split with -1 performs reverse
            nums[strt:end] = nums[strt:end][::-1]
 

arr = [1,1,5]
     
Solution().nextPermutation(arr)
     
for i in arr:
    print(i, end=" ")