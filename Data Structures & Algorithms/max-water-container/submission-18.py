class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0

        l, r = 0, len(heights) - 1

        while l <= r:
            curr_amount = min(heights[l], heights[r]) * (r - l)
            max_amount = max(curr_amount, max_amount)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_amount
        
