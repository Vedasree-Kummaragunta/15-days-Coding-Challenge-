class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")   # split by '/'

        for part in parts:
            if part == "" or part == ".":   # ignore empty & current dir
                continue
            elif part == "..":              # go one level up
                if stack:
                    stack.pop()
            else:                           # valid dir/file name
                stack.append(part)

        return "/" + "/".join(stack)
