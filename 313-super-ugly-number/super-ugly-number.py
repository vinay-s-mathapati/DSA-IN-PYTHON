class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        min_heap = [1]
        visited = {1}
        
        current_ugly = 1
        for _ in range(n):
            current_ugly = heapq.heappop(min_heap)
            for prime in primes:
                next_ugly = current_ugly * prime
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(min_heap, next_ugly)
                    
        return current_ugly