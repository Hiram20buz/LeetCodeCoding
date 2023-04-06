#20. Valid Parentheses
class Solution:
    def is_valid(self,s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

a=Solution().is_valid("(]")
print(a)
