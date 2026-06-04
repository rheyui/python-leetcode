class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Place each number at its correct index
        # 1 should be at index 0
        # 2 should be at index 1
        # ...
        for i in range(n):

            while (1 <= nums[i] <= n and
                   nums[nums[i] - 1] != nums[i]):

                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index],
                    nums[i]
                )

        # Find first missing positive
        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1
     
        