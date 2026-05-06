class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if (r - l) * min(heights[l], heights[r]) > max_amount:
                max_amount = (r - l) * min(heights[l], heights[r])
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_amount