class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = {}
        start = {}
        end = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                start[nums[i]] = i
                end[nums[i]] = i
            else:
                count[nums[i]] += 1
                end[nums[i]] = i
        res = []
        maxi = max(count.values())
        for i, j in count.items():
            if j == maxi:
                total = end[i] - start[i] + 1
                res.append(total)
        return min(res)