class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()   # remove leading spaces
        
        if not s:
            return 0

        sign = 1
        i = 0

        # Check sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0

        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = sign * num

        # Handle 32-bit integer range
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num 