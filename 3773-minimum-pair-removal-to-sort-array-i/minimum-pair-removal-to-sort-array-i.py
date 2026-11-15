class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        count = 0

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        while not is_sorted(arr):

            min_sum = float('inf')
            index = 0

            for i in range(len(arr) - 1):

                pair_sum = arr[i] + arr[i + 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i

            arr[index] = min_sum
            arr.pop(index + 1)

            count += 1

        return count