class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_map = [0] * 26
        t_freq_map = [0] * 26
        for char in s:
            s_freq_map[ord(char) - ord('a')] += 1
            #increase the count of that char in the freq map by 1

        for char in t:
            t_freq_map[ord(char) - ord('a')] += 1
            #increase the count of that char in the freq map by 1

        return s_freq_map == t_freq_map