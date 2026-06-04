class Solution:
    def divide(self, dividend, divisor):

        # Handle overflow
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Find sign
        negative = False

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        answer = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Double the divisor
            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend -= temp
            answer += multiple

        # Apply sign
        if negative:
            return -answer

        return answer