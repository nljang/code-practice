class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            diff = -(nums[i])
            left, right = i + 1, (len(nums) - 1)
            while left < right:
                if nums[left] + nums[right] < diff:
                    left += 1
                elif nums[left] + nums[right] > diff:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    

        return answer
             

            
            