class Solution:
    roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        nums = [self.roman[i] for i in s if i in self.roman]
        sum = 0
        for i in range(len(nums)):
            try:
                if (nums[i] < nums[i + 1]):
                    sum = sum - nums[i]
                else:
                    sum = sum + nums[i]
            except Exception as e:
                sum = sum + nums[i]
        return sum


num = "MCMXCIV"
a = Solution().romanToInt(num)
print(a)