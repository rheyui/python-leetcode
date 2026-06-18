class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []

        def valid(part):
            # No leading zeros unless the number is exactly 0
            if len(part) > 1 and part[0] == '0':
                return False

            return 0 <= int(part) <= 255

        def backtrack(idx, parts, curr):
            # If 4 parts are formed
            if parts == 4:
                if idx == len(s):
                    ans.append(".".join(curr))
                return

            # Try segments of length 1, 2, and 3
            for length in range(1, 4):
                if idx + length > len(s):
                    break

                part = s[idx:idx + length]

                if valid(part):
                    curr.append(part)
                    backtrack(idx + length, parts + 1, curr)
                    curr.pop()  # backtrack

        # Quick pruning
        if len(s) < 4 or len(s) > 12:
            return []

        backtrack(0, 0, [])
        return ans