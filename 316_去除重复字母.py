import collections

class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], '')) if s else ''

class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = ['a']
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack[1:])
