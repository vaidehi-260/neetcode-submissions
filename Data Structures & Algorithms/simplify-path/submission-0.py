class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        parts = path.split('/')
        for a in parts:
            if a == "" or a==".":
                continue
            elif a == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(a)
        return "/"+"/".join(stack)