class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if not stack:
                stack.append(char)
            elif char in close_to_open:
                if close_to_open[char] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(char)
        
        if not stack:
            return True
        return False

