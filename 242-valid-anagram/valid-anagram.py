class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = {}
        # Count frequencies of characters in s
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
         # Decrease frequencies using t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        return True
        