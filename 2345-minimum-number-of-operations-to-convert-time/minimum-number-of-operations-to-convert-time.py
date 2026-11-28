class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1 = int(current[:2])
        m1 = int(current[3:])

        h2 = int(correct[:2])
        m2 = int(correct[3:])

        t1 = h1 * 60 + m1
        t2 = h2 * 60 + m2

        diff = t2-t1
        count = 0
        for i in [60, 15, 5, 1]:
            count += diff // i
            diff = diff % i
        return count