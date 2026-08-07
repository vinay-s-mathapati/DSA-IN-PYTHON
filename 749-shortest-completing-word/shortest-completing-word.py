class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        req = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        result = None
        for word in words:
            wc = Counter(word)
            if all(wc[c] >= req[c] for c in req):
                if result is None or len(word) < len(result):
                    result = word
        return result