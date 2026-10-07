class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            left = i + 1
            right = n - i
            odd_count = (left * right + 1)//2
            ans += arr[i] * odd_count
        return ans
