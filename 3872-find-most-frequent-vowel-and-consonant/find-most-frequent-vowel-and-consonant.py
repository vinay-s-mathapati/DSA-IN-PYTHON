class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        vowels = set('aeiou')

        max_vowel = 0
        max_consonant = 0

        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)
        return max_vowel + max_consonant