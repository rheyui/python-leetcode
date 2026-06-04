from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_map = Counter(words)
        ans = []

        # Try all possible starting positions
        for i in range(word_len):

            left = i
            curr_map = Counter()
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                # Valid word
                if word in word_map:
                    curr_map[word] += 1
                    count += 1

                    # Remove extra occurrences
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Found valid substring
                    if count == total_words:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # Reset window
                    curr_map.clear()
                    count = 0
                    left = right + word_len

        return ans
        