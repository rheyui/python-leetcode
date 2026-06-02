class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i = 0
        j = 0
        
        # Merge step
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        n = len(merged)
        
        # Compute median
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2.0
        else:
            return float(merged[n//2])
