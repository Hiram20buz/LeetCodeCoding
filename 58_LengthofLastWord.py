class Solution:
    '''
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        # Start iterating from the end of the string
        for i in range(len(s) - 1, -1, -1):
            # Check for non-space characters
            if s[i] != ' ':
                length += 1
            # Break loop when a space is encountered after finding the last word
            elif length > 0:
                break
        return length
    '''
    def lengthOfLastWord(self, s: str) -> int:
        return len(next((word for word in reversed(s.split()) if word), ''))


s = "   fly me   to   the moon  "
a = Solution().lengthOfLastWord(s)
print(a)