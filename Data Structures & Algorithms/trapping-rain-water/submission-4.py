class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1

        answer, max_left, max_right = 0, height[l], height[r]

        while l < r:
            if height[l] <= height[r]:
                l += 1
                max_left = max(max_left, height[l])
                answer += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                answer += max_right - height[r]
        return answer
