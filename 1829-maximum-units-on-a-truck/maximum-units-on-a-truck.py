class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        total_units = 0
        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            total_units += take * units
            truckSize -= take
        return total_units