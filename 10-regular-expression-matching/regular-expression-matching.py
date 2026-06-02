class Solution(object):
    def isMatch(self, s, p):
        
        memo = {}

        def dp(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is finished
            if j == len(p):
                return i == len(s)

            # Check current match
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                
                # Two choices:
                # 1. Skip x*
                # 2. Use x* if first character matches
                ans = dp(i, j + 2) or (
                    first_match and dp(i + 1, j)
                )

            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
        