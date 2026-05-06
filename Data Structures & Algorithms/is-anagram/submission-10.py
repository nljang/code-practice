class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):  #or t doesnt matter since both same length
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        
        return hashmapS == hashmapT

        