class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        current_position = 0
        for i in word:
            target_position = ord(i) - ord('a')
            distance = abs(current_position - target_position)
            min_distance = min(distance, 26 - distance)
            total_time = total_time + min_distance
            total_time = total_time + 1
            current_position = target_position
        return total_time 