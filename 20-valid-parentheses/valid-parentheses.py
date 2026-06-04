class Solution(object):
    def isValid(self, s):
        # This approach ONLY works for simple cases without nesting
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return len(s) == 0
