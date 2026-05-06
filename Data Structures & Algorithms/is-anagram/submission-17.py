class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqmap = [0] * 26
        t_freqmap = [0] * 26

        for char in s:
            s_freqmap[ord(char) - ord('a')] += 1
        
        for char in t:
            t_freqmap[ord(char) - ord('a')] += 1
        
        return s_freqmap == t_freqmap
