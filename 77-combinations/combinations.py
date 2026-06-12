class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)          # choose
                backtrack(num + 1, path) # explore
                path.pop()               # unchoose

        backtrack(1, [])
        return result