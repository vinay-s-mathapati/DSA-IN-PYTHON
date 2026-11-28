class Solution:
    def fillCups(self, amount: list[int]) -> int:
        total = sum(amount)
        maxi = max(amount)
        return max(maxi, (total+1)//2)