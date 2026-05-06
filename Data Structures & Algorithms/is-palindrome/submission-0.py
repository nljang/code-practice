class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        normal_spelling = ''
        for char in s:
            if char.isalnum():
                normal_spelling += char.lower() #lowercases everything in case of capitals

        return normal_spelling == normal_spelling[::-1]