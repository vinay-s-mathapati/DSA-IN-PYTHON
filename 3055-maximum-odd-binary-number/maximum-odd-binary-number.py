class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = s.count("0")
        first = "1" *(ones-1)
        middle = "0" * zeros
        last = "1"
        result = first + middle + last
        return result