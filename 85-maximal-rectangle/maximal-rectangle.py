from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest Rectangle in Histogram
            stack = []
            for i in range(cols + 1):
                curr_height = 0 if i == cols else heights[i]

                while stack and heights[stack[-1]] > curr_height:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area  