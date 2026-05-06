class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char in close_to_open:
                    if stack[-1] == close_to_open[char]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    stack.append(char)
        
        if not stack:
            return True
        return False
