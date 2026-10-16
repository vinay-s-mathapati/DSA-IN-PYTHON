class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i in range(len(nums)):
            position = index[i]
            value = nums[i]
            target.insert(position, value)
        return target