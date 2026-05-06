class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_map = [0] * 26
        t_freq_map = [0] * 26

        for i in range(len(s)):
            s_freq_map[ord(s[i]) - ord('a')] += 1
            t_freq_map[ord(t[i]) - ord('a')] += 1
        
        return s_freq_map == t_freq_map
