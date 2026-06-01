class Solution:
    def combinationSum2(self, candidates, target):
        
        candidates.sort()
        ans = []

        def backtrack(start, path, total):

            if total == target:
                ans.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                backtrack(i + 1, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)

        return ans