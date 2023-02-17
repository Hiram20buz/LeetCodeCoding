class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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
        
        #a=self.median(arr3)
        
        # initializing list
        #test_list = [4, 5, 8, 9, 10, 17]
        # Median of list
        # Using statistics.median()
        mid = len(arr3) // 2
        res = (arr3[mid] + arr3[~mid]) / 2
         
        # Printing result
        a=float(res)
        return a
        
        
        
#nums1 = [1,2]
#nums2 = [3,4]
ans=Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
print(ans)
