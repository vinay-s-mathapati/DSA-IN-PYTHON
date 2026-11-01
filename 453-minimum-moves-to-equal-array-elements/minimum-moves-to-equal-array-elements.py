class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_ = min(nums)
        n = len(nums)
        total = sum(nums)
        return total - (n*min_)