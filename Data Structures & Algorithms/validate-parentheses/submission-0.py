class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["[", "(", "{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    if not ((c == "]" and top == "[")
                    or (c == "}" and top == "{") 
                    or (c == ")" and top == "(")):
                        return False
                    else:
                        stack.pop()
        
        return not stack