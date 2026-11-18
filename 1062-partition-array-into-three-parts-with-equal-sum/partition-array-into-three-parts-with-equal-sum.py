class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        count = 0
        running_sum = 0
        for i, num in enumerate(arr):
            running_sum += num
            if running_sum == target and count < 2 and i < len(arr) - 1:
                count += 1
                running_sum = 0
        return count >= 2
