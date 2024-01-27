class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        n = x
        while True:
            root = 0.5 * (n + x / n)
            if abs(root - n) < 0.0001:
                return int(root)
            n = root

a = Solution().mySqrt(4)
print(a)
