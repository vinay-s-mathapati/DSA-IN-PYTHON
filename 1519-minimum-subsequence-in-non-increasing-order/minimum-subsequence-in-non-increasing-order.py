class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        sorted_nums = sorted(nums, reverse = True)
        selected_sum = 0
        result = []
        for num in sorted_nums:
            
            selected_sum += num
            result.append(num)
            if selected_sum > total - selected_sum:
                break
        return result

