class Solution:
    def judgeCircle(self, moves: str) -> bool:
        for i in range(len(moves)):
            if moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L'):

                return True
            return False
            