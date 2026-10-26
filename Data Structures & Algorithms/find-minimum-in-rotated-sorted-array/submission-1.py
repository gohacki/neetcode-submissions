class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 9999
        if nums[l] <= nums[r]:
            return nums[l]
        while r > l:
            m = (r + l) // 2
            if nums[m] > nums[l]:
                res = min(res, nums[l])
                l = m
            elif nums[m] < nums[l]:
                res = min(res, nums[m])
                r = m
            else:
                return min(res, nums[l], nums[r])
