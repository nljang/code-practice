class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for character in range(len(s)):
            count_s[s[character]] = 1 + count_s.get(s[character], 0)
            count_t[t[character]] = 1 + count_t.get(t[character], 0)
        
        return count_s == count_t

        
