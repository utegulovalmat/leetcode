class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = collections.Counter(chars)
        res = 0
        for word in words:
            all_there = True
            counter = [0] * 26
            for w in word:
                idx = ord(w) - ord('a')
                counter[idx] += 1
                if w not in chars or chars[w] < counter[idx]:
                    all_there = False
                    break
            if all_there:
                res += len(word)
        return res