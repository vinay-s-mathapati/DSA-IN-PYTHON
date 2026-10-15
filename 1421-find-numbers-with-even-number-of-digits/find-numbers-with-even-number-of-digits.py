class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        res = []
        for i in range (len(nums)):
            if len(str(abs(nums[i]))) % 2 == 0:
                res.append(nums[i])
        return len(res)
            