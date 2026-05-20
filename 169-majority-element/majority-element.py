class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count = 0
       candidiate = None

       for num in nums:
        if count == 0:
            candidiate = num

        if num == candidiate:
            count += 1
        else:
            count -= 1

       return candidiate