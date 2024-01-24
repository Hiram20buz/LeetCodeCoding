num = 3999
num1 = 664

roman = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
    }

def thousands(n):
    return f"{roman[1000]}" * (n // 1000)

def hundreds(n):
    if ((n % 1000) >= 900):
        return "CM"
    elif ((n % 1000) == 500):
        return "D"
    elif ((n % 1000) < 400):
        return f"{roman[100]}" * ((n % 1000)//100)
    elif ((n % 1000) >= 400 and (n % 1000) < 500 ):
        return "CD"
    elif ((n % 1000) > 500 and (n % 1000) < 900 ):
        return "D" + f"{roman[100]}" * (((n % 1000)//100) - 5)

def tens(n):
    if ((n % 100) >= 90):
        return "XC"
    elif ((n % 100) == 50):
        return "L"
    elif ((n % 100) < 40):
        return f"{roman[10]}" * ((n % 100)//10)
    elif ((n % 100) >= 40 and (n % 100) < 50 ):
        return "XL"
    elif ((n % 100) > 50 and (n % 100) < 90 ):
        return "L" + f"{roman[10]}" * (((n % 100)//10) - 5)

def units(n):
    if ((n % 10) >= 9):
        return "IX"
    elif ((n % 10) == 5):
        return "V"
    elif ((n % 10) < 4):
        return f"{roman[1]}" * ((n % 10)//1)
    elif ((n % 10) >= 4 and (n % 10) < 5 ):
        return "IV"
    elif ((n % 10) > 5 and (n % 10) < 9 ):
        return "V" + f"{roman[1]}" * (((n % 10)//1) - 5)


print(thousands(num1) + hundreds(num1) + tens(num1) + units(num1))
