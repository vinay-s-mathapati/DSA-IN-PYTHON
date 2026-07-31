class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0   

            s = x + y + carry
            res = str(s % 10) + res
            carry = s // 10

            i -= 1
            j -= 1

        return res
       