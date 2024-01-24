num = "MCMXCIV"

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }
    
'''
nums = []
for i in num:
    if i in roman:
        nums.append(roman[i])
'''
nums = [roman[i] for i in num if i in roman]

sum = 0
for i in range(len(nums)):
    try:
        if (nums[i] < nums[i + 1]):
            sum = sum - nums[i]
        else:
            sum = sum + nums[i]
    except Exception as e:
         sum = sum + nums[i]

print(sum)
    
