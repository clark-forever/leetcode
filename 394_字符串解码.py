class Solution1:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

class Solution2:
    def decodeString(self, s: str) -> str:
        def dfs(s, index):
            res, multi = "", 0
            while index < len(s):
                if '0' <= s[index] <= '9':
                    multi = multi * 10 + int(s[index])
                elif s[index] == '[':
                    index, tmp = dfs(s, index + 1)
                    res += multi * tmp
                    multi = 0
                elif s[index] == ']':
                    return index, res
                else:
                    res += s[index]
                index += 1
            return res

        return dfs(s, 0)
