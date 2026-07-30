class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t) - Counter(s)
        return list(count.keys())[0]