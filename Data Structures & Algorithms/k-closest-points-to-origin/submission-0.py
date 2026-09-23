class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for coords in points:
            dist = (((coords[0] ** 2) + (coords[1] ** 2)) ** 1/2) * -1
            temp = (dist, coords)
            
            heapq.heappush(distances, temp)
            if len(distances) > k:
                heapq.heappop(distances)

        res = [coords for dist, coords in distances]
        return res