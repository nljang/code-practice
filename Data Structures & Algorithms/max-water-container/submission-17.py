class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            amount = (r - l) * min(heights[r], heights[l])
            max_amount = max(max_amount, amount)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
        
        return max_amount
