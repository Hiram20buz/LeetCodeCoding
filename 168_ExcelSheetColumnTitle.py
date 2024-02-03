class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnTitle = ''
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            columnTitle = chr(ord('A') + remainder) + columnTitle
        return columnTitle

a = Solution().convertToTitle(701)
print(a)