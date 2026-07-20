class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = [(score[i], i) for i in range(n)]
        arr.sort(reverse = True)
        result = [" "] * n
        for i in range(n):
            idx = arr[i][1]
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i+1)
        return result

        