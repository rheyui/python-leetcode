from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)

        result = []

        # Try every possible starting offset
        for i in range(word_len):

            left = i
            count = 0

            seen = defaultdict(int)

            # Move window in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                # Valid word
                if word in word_count:

                    seen[word] += 1
                    count += 1

                    # Too many occurrences
                    while seen[word] > word_count[word]:

                        left_word = s[left:left + word_len]

                        seen[left_word] -= 1
                        count -= 1

                        left += word_len

                    # Found valid window
                    if count == total_words:

                        result.append(left)

                        left_word = s[left:left + word_len]

                        seen[left_word] -= 1
                        count -= 1

                        left += word_len

                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result