class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #inputs: list of numbers, integer "target"
        #output: indices 'i' and 'j' whre their corresponding number in the array add to our target

        seen = {}
        for index, value in enumerate(nums):
            goal = target - value
            if goal in seen:   #make curr value the dict key, and curr index the dict value
                return [seen[goal], index]
            else:
                seen[value] = index

        #[3, 4, 5, 6] target = 7

        #index = 0, value = 3   goal 4
        #index = 1, value = 4   goal = 3
        
        #seen: index = 0, value = 3

        #return 0, 1