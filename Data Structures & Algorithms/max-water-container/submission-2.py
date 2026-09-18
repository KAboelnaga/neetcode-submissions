class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            water = min(heights[i], heights[j]) * (j - i)
            res = max(res, water)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1               
        return res