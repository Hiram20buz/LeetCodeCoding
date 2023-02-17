# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2):
    i = 0
    j = 0
    k = 0
    arr3 = [0 for i in range(len(arr1)+len(arr2))]
    #mergeArrays(arr1, arr2, arr3)
  
    # traverse the arr1 and insert its element in arr3
    while(i < len(arr1)):
        arr3[k] = arr1[i]
        k += 1
        i += 1
  
    # now traverse arr2 and insert in arr3
    while(j < len(arr2)):
        arr3[k] = arr2[j]
        k += 1
        j += 1
  
    # sort the whole array arr3
    arr3.sort()
    
    return arr3
  
  
# Driver code

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3=mergeArrays(arr1, arr2)
print("Array after merging")
for val in arr3:
    print(val)
    
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
    
a=median(arr3)

print(a)
