class Solution(object):
    def isPalindrome(self, s):
        
        text = ""

        # Keep only letters and numbers
        for ch in s:
            if ch.isalnum():
                text += ch.lower()

        # Check palindrome
        return text == text[::-1]