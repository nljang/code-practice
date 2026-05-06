class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0

        l, r = 0, 0

        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                result = max(result, len(seen))
                r += 1
            else:
                seen.remove(s[l])
                l += 1 
                

        return result




        


