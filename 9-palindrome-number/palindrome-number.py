class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)              # convert number to string
        return s == s[::-1]     # compare with reversed string
