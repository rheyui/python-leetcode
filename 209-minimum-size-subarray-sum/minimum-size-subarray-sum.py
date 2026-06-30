class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        minimumsize = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                minimumsize = min(minimumsize, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if minimumsize == float('inf'):
            return 0
        return minimumsize