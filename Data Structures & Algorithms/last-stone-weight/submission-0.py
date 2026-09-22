class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones) 

            if s1 < s2:
                s1 -= s2
                heapq.heappush(stones, s1)
            elif s1 > s2:
                s2 -= s1
                heapq.heappush(stones, s2)

        if len(stones) > 0:
            return heapq.heappop(stones) * -1
        
        return 0
            