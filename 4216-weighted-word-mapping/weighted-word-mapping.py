class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            val = total % 26
            mapped_char = chr(ord('z') - val)

            res.append(mapped_char)
        return "".join(res)