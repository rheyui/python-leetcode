class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > curr_height:
                h = heights[stack.pop()]

                left = stack[-1] if stack else -1
                width = i - left - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area