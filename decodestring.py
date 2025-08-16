 class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)   # handle multi-digit numbers
            elif ch == '[':
                stack.append((cur_str, cur_num))
                cur_str, cur_num = "", 0
            elif ch == ']':
                prev_str, num = stack.pop()
                cur_str = prev_str + num * cur_str
            else:
                cur_str += ch

        return cur_str
