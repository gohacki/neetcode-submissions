class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        cur = 0
        for num in nums:
            if target - num in seen:
                return [seen[target - num], cur]
            seen[num] = cur
            cur += 1