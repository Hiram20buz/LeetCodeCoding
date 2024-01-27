class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        #Transposed Matrix
        transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
        #Mirrored Matrix
        matrix[:] = [row[::-1] for row in transposed]


# Example matrix
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

a = Solution().rotate(matrix)

for row in matrix:
    print(row)
