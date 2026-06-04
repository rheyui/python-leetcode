class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_string):
            
            # Base case
            if index == len(digits):
                result.append(current_string)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            
            for letter in letters:
                backtrack(index + 1, current_string + letter)
        
        backtrack(0, "")
        return result