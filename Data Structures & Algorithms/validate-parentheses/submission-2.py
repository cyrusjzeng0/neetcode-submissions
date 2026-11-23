class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        for c in s:
            if c in maps:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    if maps[top] != c:
                        return False
                    else:
                        stack.pop()
        
        return not stack