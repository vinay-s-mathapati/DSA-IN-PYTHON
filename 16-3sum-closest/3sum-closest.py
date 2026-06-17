class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i+1, n-1
            while l < h:
                curr_sum = nums[i] + nums[l] + nums[h]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    h -= 1
        return closest_sum