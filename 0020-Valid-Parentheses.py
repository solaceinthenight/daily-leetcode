class Solution:
    isValid(self, s: str) -> bool:
        stack = []
        for i, c in enumerate(s):
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            elif len(stack) > 0:
                char = stack.pop()
                if c == ')' and char != '(':
                    return False
                elif c == '}' and char != '{':
                    return False
                elif c == ']' and char != '[':
                    return False
            else:
                return False
        return len(stack) == 0
