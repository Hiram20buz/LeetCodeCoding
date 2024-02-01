class Solution:
    roman = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
    }

    
    def intToRoman(self, num: int) -> str:
        return self.thousands(num) + self.hundreds(num) + self.tens(num) + self.units(num)

    def thousands(self, n):
        return f"{self.roman[1000]}" * (n // 1000)

    def hundreds(self, n):
        if ((n % 1000) >= 900):
            return "CM"
        elif ((n % 1000) == 500):
            return "D"
        elif ((n % 1000) < 400):
            return f"{self.roman[100]}" * ((n % 1000)//100)
        elif ((n % 1000) >= 400 and (n % 1000) < 500 ):
            return "CD"
        elif ((n % 1000) > 500 and (n % 1000) < 900 ):
            return "D" + f"{self.roman[100]}" * (((n % 1000)//100) - 5)

    def tens(self, n):
        if ((n % 100) >= 90):
            return "XC"
        elif ((n % 100) == 50):
            return "L"
        elif ((n % 100) < 40):
            return f"{self.roman[10]}" * ((n % 100)//10)
        elif ((n % 100) >= 40 and (n % 100) < 50 ):
            return "XL"
        elif ((n % 100) > 50 and (n % 100) < 90 ):
            return "L" + f"{self.roman[10]}" * (((n % 100)//10) - 5)

    def units(self, n):
        if ((n % 10) >= 9):
            return "IX"
        elif ((n % 10) == 5):
            return "V"
        elif ((n % 10) < 4):
            return f"{self.roman[1]}" * ((n % 10)//1)
        elif ((n % 10) >= 4 and (n % 10) < 5 ):
            return "IV"
        elif ((n % 10) > 5 and (n % 10) < 9 ):
            return "V" + f"{self.roman[1]}" * (((n % 10)//1) - 5)



num = 3999
a = Solution().intToRoman(num)
print(a)
