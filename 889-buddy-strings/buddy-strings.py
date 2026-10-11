class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        mismatch = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatch.append(i)
        if len(mismatch) == 2:
            i, j = mismatch[0], mismatch[1]
            return s[i] == goal[j] and s[j] == goal[i]
        return False