class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        res = ''
        for idx, char in enumerate(s):
            if char == ' ':
                res += ''.join(reversed(word)) + ' '
                word = []
            else:
                word.append(s[idx])
        res += ''.join(reversed(word))
        return res