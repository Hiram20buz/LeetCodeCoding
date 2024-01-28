'''
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            return list(map(int, str(int(''.join(map(str, digits))) + 1)))
'''
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            if digits[i] == 9:
                digits[i] = 0
        if digits[0] == 0:
            digits = [1] + digits
        return digits


a = Solution().plusOne([8,9,9,9])
print(a)
