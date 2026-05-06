class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        left, right = 0, len(heights) - 1
        while left < right:
            current_amount = (right - left) * min(heights[left], heights[right])
            if current_amount > max_amount:
                max_amount = current_amount
                
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
            
        return max_amount

