class Solution:
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(start, path, total):
            # if target achieved
            if total == target:
                result.append(path[:])
                return
            # if total exceeds target
            if total > target:
                return
            # try all candidates starting from current index
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return result