# 11. Container With Most Water
class Solution:
    def print2largest(self,arr, arr_size):
        # There should be atleast
        # two elements
    	if (arr_size < 2):
    	
    		print(" Invalid Input ")
    		return
    	
    
    	first = second = -2147483648
    	for i in range(arr_size):
    	
    		# If current element is
    				# smaller than first
    		# then update both
    				# first and second
    		if (arr[i] > first):
    		
    			second = first
    			first = arr[i]
    		
    
    		# If arr[i] is in
    				# between first and
    		# second then update second
    		elif (arr[i] > second and arr[i] != first):
    			second = arr[i]
    	
    	if (second == -2147483648):
    		#print("There is no second largest element")
    		return 0
    	else:
    		#print("The second largest element is", second)
    		return second
    		
    def indices(self,lst, item):
        return [i for i, x in enumerate(lst) if x == item]
        
    def maxArea(self, height: list[int]) -> int:
        result=[]
        
        dif=self.indices(height, max(height))
        base=dif[len(dif)-1]-dif[0]
        result.append(base*max(height))
        
        n = len(height)
        dif1=self.indices(height,self.print2largest(height, n) )
        base=dif1[len(dif1)-1]-dif1[0]
        result.append(base*self.print2largest(height, n))
        
        if(min(dif) < min(dif1)):
            base=dif1[len(dif1)-1]-dif[0]
            result.append(base*self.print2largest(height, n))
            
            
        return max(result)
        
      
  
a=Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])

print(a)
