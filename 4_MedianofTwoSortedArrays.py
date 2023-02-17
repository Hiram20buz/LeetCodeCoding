class Solution(object):
    def median(self,lst):
        n = len(lst)
        s = sorted(lst)
        return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
    
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        k = 0
        arr3 = [0 for i in range(len(nums1)+len(nums2))]
        #mergeArrays(arr1, arr2, arr3)
      
        # traverse the arr1 and insert its element in arr3
        while(i < len(nums1)):
            arr3[k] = nums1[i]
            k += 1
            i += 1
      
        # now traverse arr2 and insert in arr3
        while(j < len(nums2)):
            arr3[k] = nums2[j]
            k += 1
            j += 1
      
        # sort the whole array arr3
        arr3.sort()
        
        a=self.median(arr3)
        return a
        
        
#nums1 = [1,2]
#nums2 = [3,4]
ans=Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
print(ans)
            
