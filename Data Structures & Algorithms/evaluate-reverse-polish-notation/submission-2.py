class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in ('+','-','*','/'):
                stack.append(int(char))
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            if char == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            if char == '*':
                stack.append(stack.pop() * stack.pop())
            if char == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))   #int rounds down to 0
        
        return stack[-1]

