class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0) #for each character add 1 to..
            count_t[t[i]] = 1 + count_t.get(t[i], 0) # the count of whatevers there already

        for j in count_s:
            if count_s[j] != count_t.get(j, 0):
                return False
        
        return True
