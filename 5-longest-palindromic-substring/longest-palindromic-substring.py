class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        start = 0
        max_len = 1
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            # Even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        return s[start:start + max_len]

        