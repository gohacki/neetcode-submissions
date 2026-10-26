class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            # If the middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the minimum is in the left half (including m).
            else:
                r = m
                
        return nums[l]