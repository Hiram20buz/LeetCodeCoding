class Solution(object):
    def twoSum(self, nums, target):
        '''
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        '''
        
        self.nums = nums
        self.target = target
        indices=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] + nums[j] == target and i!=j and (i or j) not in indices):
                    indices.append(i)
                    indices.append(j)
                    break
        
        return indices
                    
                    
audi = Solution()

ind=audi.twoSum([2,7,11,15], 9)
print(ind)
