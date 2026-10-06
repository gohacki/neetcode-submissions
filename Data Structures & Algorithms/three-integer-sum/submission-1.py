class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            front = i + 1
            back = len(nums) - 1
            if i > len(nums) - 3:
                break
            while front < back:
                if n + nums[front] + nums[back] == 0:
                    res.append([n, nums[front], nums[back]])
                    front += 1
                    while front < len(nums) - 1 and nums[front] == nums[front-1]:
                        front += 1
                elif n + nums[front] + nums[back] < 0:
                    front += 1
                else:
                    back -= 1
                    while back > 0 and nums[back] == nums[back+1]:
                        back -= 1
        return res 
            
