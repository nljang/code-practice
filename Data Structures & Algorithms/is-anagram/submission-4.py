class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for char in s:
            s_list.append(char)
        
        for char in t:
            t_list.append(char)

        if sorted(s_list) == sorted(t_list):
            return True
        return False