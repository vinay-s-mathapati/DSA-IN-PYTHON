class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        lenght = 0
        for val in count.values():
            lenght += (val//2) * 2
        if lenght < len(s):
            lenght += 1
        return lenght