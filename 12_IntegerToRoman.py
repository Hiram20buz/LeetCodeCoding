num = 3999

thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
units = (num % 10)

print(thousands, hundreds, tens, units)
# expected output: 1 2 3 4
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
        }
        
def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 
    
print(get_nth_key(roman, 0))
print(list(roman.keys()).index("D"))

if(900-roman['D']>300):
    if(roman['M']-roman['C']==900):
        print("CM")
    
'''
if(int(num/roman['M'])<4):
            print('M'*int(num/roman['M']))
            num=num%roman['M']
            
'''
