class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            print(stack)
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                if stack:
                    last = stack.pop()
                else:
                    return False
                if char == ']':
                    if last == '[':
                        continue
                    else: return False
                elif char == '}':
                    if last == '{':
                        continue
                    else: return False
                elif char == ')':
                    if last == '(':
                        continue
                    else: return False
        if stack:
            return False
        return True
        
