class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        num = set(nums)
        if 0 in num:
            num.remove(0)
        return len(num)