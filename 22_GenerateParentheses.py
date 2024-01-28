'''
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
'''
1 <= n <= 8

'''
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

'''
#n = int(input())

def p(ln, rn):
    l = '('
    r = ')'
    return (l*ln) + (r*rn)


print(p(1,0) * 2 + p(1,1) * 1 + p(0,1) * 2)

print(p(1,0) * 1 + p(1,1) * 2 + p(0,1) * 1)

print(p(1,0) * 2 + p(0,1) * 2 + p(1,1) * 1)

print(p(1,1) * 1 + p(1,0) * 2 + p(0,1) * 2)

print(p(1,1) * 1 + p(1,1) * 1 + p(1,1) * 1)
'''
#centro
print(p(1,0) * 2 + p(1,1) * 1 + p(0,1) * 2)
print(p(1,0) * 1 + p(1,1) * 2 + p(0,1) * 1)
'''