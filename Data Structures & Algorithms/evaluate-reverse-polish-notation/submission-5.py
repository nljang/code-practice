class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if not stack:
                stack.append(int(char))
            else:
                if char not in ['+', '-', '*', '/']:
                    stack.append(int(char))
                elif char == '+':
                    stack.append(stack.pop() + stack.pop())
                elif char == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif char == '*':
                    stack.append(stack.pop() * stack.pop())
                elif char == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
        return stack[-1]