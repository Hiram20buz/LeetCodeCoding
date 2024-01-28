class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_string = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                result_string += char.lower()
        return result_string == result_string[::-1]


input_string = "race a car"
a = Solution().isPalindrome(input_string)
print(a)