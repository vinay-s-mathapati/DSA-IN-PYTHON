class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            max_val = min_val = nums[i]
            for j in range(i):
                max_val = max(max_val, nums[j])
            for j in range(i+1, n):
                min_val = min(min_val, nums[j])
            if max_val - min_val <= k:
                return i
        return -1
       