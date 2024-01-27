class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle special cases
        if divisor == 0:
            raise ZeroDivisionError
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the quotient
        neg = (dividend < 0) ^ (divisor < 0)

        # Convert both dividend and divisor to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize quotient and current remainder
        quotient = 0
        current_remainder = dividend

        # Subtract multiples of the divisor from the current remainder
        while current_remainder >= divisor:
            # Find the largest multiple of divisor that is less than or equal to the current remainder
            shift = 0
            while (divisor << shift) <= current_remainder:
                shift += 1
            shift -= 1

            # Subtract the multiple from the current remainder and update the quotient
            quotient += 1 << shift
            current_remainder -= divisor << shift

        # Apply the sign to the quotient and return it
        return -quotient if neg else quotient

print(Solution().divide(10,3))
