class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = ""
        if num < 0:
            sign = "-"
            num = - num
        result = ""
        while num > 0:
            result += str(num%7)
            num //= 7
        return sign + result[::-1]