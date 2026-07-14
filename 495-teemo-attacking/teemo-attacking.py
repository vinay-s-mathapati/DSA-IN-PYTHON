class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        t = len(timeSeries)
        for i in range(t-1):
            gap = timeSeries[i+1] - timeSeries[i]
            
            total += min(duration, gap)
        total += duration
        return total