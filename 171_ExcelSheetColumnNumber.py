class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        for char in columnTitle:
            columnNumber = columnNumber * 26 + (ord(char) - ord('A') + 1)
        return columnNumber


columnTitle = "ZY"
columnNumber = Solution().titleToNumber(columnTitle)
print(columnNumber)