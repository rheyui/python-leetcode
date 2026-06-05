class Solution(object):
    def nextPermutation(self, nums):

        # Start from second last index
        i = len(nums) - 2

        # Find first smaller number from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such number exists
        if i >= 0:

            # Start from last index
            j = len(nums) - 1

            # Find number bigger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1

            # Swap both numbers
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the right part
        nums[i + 1:] = nums[i + 1:][::-1]
        