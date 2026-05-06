class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for i in s:
            s_list.append(i)

        for i in t:
            t_list.append(i)
        
        if sorted(s_list) == sorted(t_list):
            return True
        else:
            return False
        

        



        
        