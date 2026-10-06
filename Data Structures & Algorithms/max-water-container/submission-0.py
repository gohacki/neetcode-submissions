class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        front, back = 0, len(heights) - 1
        while front < back:
            volume = min(heights[front], heights[back]) * (back - front)
            if volume > res:
                res = volume
            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1
        return res
            