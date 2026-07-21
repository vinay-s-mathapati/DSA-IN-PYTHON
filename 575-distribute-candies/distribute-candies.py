class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        res = set(candyType)
        res2 =  len(res)
        res1 = len(candyType)//2
        return min(res2, res1)
        
