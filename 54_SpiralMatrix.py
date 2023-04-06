#54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return self.spiralMatrixPrint(len(matrix), len(matrix[0]), matrix)
        
    def spiralMatrixPrint(self,row, col, arr):
        result=[]
        # Defining the boundaries of the matrix.
        top = 0
        bottom = row-1
        left = 0
        right = col - 1
    
        # Defining the direction in which the array is to be traversed.
        dir = 0
        
        while (top <= bottom and left <=right):    
            if dir ==0:
                for i in range(left,right+1): # moving left->right
                    result.append(arr[top][i])
    
                # Since we have traversed the whole first
                # row, move down to the next row.
                top +=1
                dir = 1
    
            elif dir ==1:
                for i in range(top,bottom+1): # moving top->bottom
                    result.append(arr[i][right])
    
                # Since we have traversed the whole last
                # column, move down to the previous column.
                right -=1 
                dir = 2
                
            elif dir ==2:
                for i in range(right,left-1,-1): # moving right->left
                    result.append(arr[bottom][i])
    
                # Since we have traversed the whole last
                # row, move down to the previous row.
                bottom -=1
                dir = 3
                
            elif dir ==3:
                for i in range(bottom,top-1,-1): # moving bottom->top
                    result.append(arr[i][left])
                # Since we have traversed the whole first
                # column, move down to the next column.
                left +=1
                dir = 0
        
        return result
    
    
array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]
    
a=Solution().spiralOrder(array)
print(a)
